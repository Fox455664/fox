import config
from git import Repo, InvalidGitRepositoryError, GitCommandError
import logging
import subprocess

# إعداد سجل البيانات
LOGGER = logging.getLogger(__name__)

def git():
    # الحصول على رابط المستودع والتوكن من وحدة config
    REPO_LINK = config.UPSTREAM_REPO
    GIT_TOKEN = config.GIT_TOKEN

    if not REPO_LINK:
        LOGGER.error("REPO_LINK غير معرف. يرجى التحقق من إعدادات config.")
        return
    
    if GIT_TOKEN:
        try:
            GIT_USERNAME = REPO_LINK.split("com/")[1].split("/")[0]
            TEMP_REPO = REPO_LINK.split("https://")[1]
            UPSTREAM_REPO = f"https://{GIT_USERNAME}:{GIT_TOKEN}@{TEMP_REPO}"
        except IndexError:
            LOGGER.error("تنسيق REPO_LINK غير صحيح.")
            return
    else:
        UPSTREAM_REPO = REPO_LINK

    try:
        # محاولة فتح مستودع Git
        repo = Repo()
        LOGGER.info("تم العثور على عميل Git [VPS DEPLOYER]")
    except InvalidGitRepositoryError:
        LOGGER.info("لم يتم العثور على مستودع Git صالح، جاري تهيئة مستودع جديد.")
        repo = Repo.init()
        try:
            origin = repo.create_remote("origin", UPSTREAM_REPO)
            origin.fetch()
        except Exception as e:
            LOGGER.error(f"فشل إنشاء أو جلب من البعيد: {e}")
            return

        if config.UPSTREAM_BRANCH not in repo.heads:
            repo.create_head(config.UPSTREAM_BRANCH, origin.refs[config.UPSTREAM_BRANCH])
        repo.heads[config.UPSTREAM_BRANCH].set_tracking_branch(origin.refs[config.UPSTREAM_BRANCH])
        repo.heads[config.UPSTREAM_BRANCH].checkout(True)

    try:
        # محاولة جلب وسحب التحديثات من المستودع البعيد
        origin = repo.remotes.origin
        origin.fetch(config.UPSTREAM_BRANCH)
        origin.pull(config.UPSTREAM_BRANCH)
        LOGGER.info("تم جلب وسحب التحديثات بنجاح.")
    except GitCommandError as e:
        LOGGER.error(f"فشل السحب من Git: {e}")
        try:
            repo.git.reset("--hard", "FETCH_HEAD")
        except GitCommandError as reset_error:
            LOGGER.error(f"فشل إعادة تعيين Git: {reset_error}")

    # تثبيت المتطلبات
    stdout, stderr, returncode = install_req("pip3 install --no-cache-dir -r requirements.txt")
    if returncode == 0:
        LOGGER.info("تم تثبيت المتطلبات بنجاح.")
    else:
        LOGGER.error(f"خطأ في تثبيت المتطلبات: {stderr}")

    LOGGER.info("جاري جلب التحديثات من المستودع البعيد...")

def install_req(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout, result.stderr, result.returncode
