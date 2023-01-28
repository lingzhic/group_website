from fabric import task
from invoke import Responder

from _credentials import github_password, github_username


def _get_github_auth_responders():
    """
    返回 GitHub 用户名密码自动填充器
    """
    username_responder = Responder(
        pattern="Username for 'https://github.com':",
        response='{}\n'.format(github_username)
    )
    password_responder = Responder(
        pattern="Password for 'https://{}@github.com':".format(github_username),
        response='{}\n'.format(github_password)
    )
    return [username_responder, password_responder]


@task()
def deploy(c):
    supervisor_conf_path = '~/etc/'
    supervisor_program_name = 'webproject'

    project_root_path = '~/apps/group_website/'

    # 先停止应用
    with c.cd(project_root_path):
        cmd = '~/.local/bin/supervisorctl -c ~/etc/supervisord.conf stop {}'.format(supervisor_program_name)
        c.run(cmd)

    # 这里你可能注意到了supervisorctl这个command是使用的从absolute path直接调用的，
    # 是因为如果直接使用单一的supervisorctl在fabric中会报错，我也不知道为什么
    # 但是使用absolute path就work了，很迷

    # 进入项目根目录，从 Git 拉取最新代码
    with c.cd(project_root_path):
        cmd = 'git pull'
        responders = _get_github_auth_responders()
        c.run(cmd, watchers=responders)

    # 重新启动应用
    with c.cd(supervisor_conf_path):
        cmd = '~/.local/bin/supervisorctl -c ~/etc/supervisord.conf start {}'.format(supervisor_program_name)
        c.run(cmd)
