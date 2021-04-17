DATA_SHEET = [
    'tb_web_user', 'tb_task_detail', 'tb_task_result', 'tb_tg_account', 'tb_tw_account', 'tb_fb_account']
DATA_SHEET_FIELD = {
    'tb_web_user': ['name', 'passwd', 'role', 'email', 'bio', 'err_count', 'login_time', 'update_time'],
    'tb_task_detail': ['task_id', 'task_user', 'task_type', 'sub_type', 'key_word', 'sub_word',
                       'opt_userinfo', 'opt_friends', 'opt_posts', 'opt_comments', 'opt_media',
                       'opt_likes', 'opt_retweets', 'status', 'update_time'],
    'tb_task_result': ['task_id', 'task_user', 'task_type', 'thread_id', 'status', 'Rate', 'task_desc',  # TODO：Rate
                       'task_result', 'start_time', 'end_time', 'update_time'],
    'tb_tg_account': ['telnumber', 'appid', 'secretkey', 'status', 'reg_time', 'update_time'],
    'tb_tw_account': ['telnumber', 'user_name', 'email', 'passwd', 'cookie', 'authorization', 'token',
                      'status', 'reg_time', 'update_time'],
    'tb_fb_account': ['telnumber', 'user_name', 'email', 'passwd', 'status', 'reg_time', 'update_time'],
}
DATA_SHEET_FIELD_REQUIRED = {
    'tb_web_user': ['name', 'passwd', 'role', 'email'],
    'tb_task_detail': ['task_id', 'task_user', 'task_type', 'key_word', 'status'],
    'tb_task_result': ['task_id', 'task_user', 'task_type', 'thread_id', 'status'],
    'tb_tg_account': ['telnumber', 'appid', 'secretkey', 'status',],
    'tb_tw_account': ['telnumber', 'user_name', 'email', 'passwd', 'status'],
    'tb_fb_account': ['telnumber', 'user_name', 'email', 'passwd', 'status'],
}
DATA_SHEET_FIELD_KEY = {
    'tb_web_user': 'name',
    'tb_task_detail': 'task_id',
    'tb_task_result': 'task_id',
    'tb_tg_account': 'telnumber',
    'tb_tw_account': 'telnumber',
    'tb_fb_account': 'telnumber',
}

DATA_SHEET_TIME_REG = ['reg_time', 'start_time']
DATA_SHEET_TIME_UPDATA = ['update_time', 'login_time', 'end_time']