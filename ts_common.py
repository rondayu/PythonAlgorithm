from mysql import connector
from datetime import datetime
from database import *
import json
SQL_LINK = ''
SQL_PWD = ''


class CommonModule(object):
    def __init__(self):
        self.conn = connector.connect(host='Simspider_003f',
                                      port=3306,
                                      user='sim',
                                      password='sim@123456',
                                      database='spider',
                                      use_unicode=True,
                                      auth_plugin='mysql_native_password')
        self.cursor = self.conn.cursor()
        print()

    def query_sheet_count(self, q_sheet):
        """
        查询表的个数
        :param q_sheet: 表名
        :return: 返回个数，返回None时表名不存在
        """
        if q_sheet not in DATA_SHEET:
            print('error: no sheet exist')
            return None
        values = 0
        sql_str = 'select count(*) from %s' % q_sheet
        try:
            self.cursor.execute(sql_str)
            values = self.cursor.fetchall()
        except BaseException as e:
            print('error: sql_str (%s)\n%s' % (sql_str, e))
            print(datetime.now().strftime('%Y%m%d%H%M%S'))
        return values

    def query_sheet_item(self, q_sheet, **kwargs):
        """
        查询单个item，必须以主键查询，不允许不能唯一确定的查询   # TODO： 添加限制
        :param q_sheet: 表名
        :param kwargs: 查询对象的条件
        :return: 返回单个item，返回False时表名不存在或无查询结果
        """
        if q_sheet not in DATA_SHEET:
            print('error: no sheet exist')
            return False
        sql_str = 'select * from %s where ' % q_sheet
        values_list = []
        for key in kwargs.keys():
            value = kwargs[key]
            if key not in DATA_SHEET_FIELD[q_sheet]:
                print('alarm: {0} not exist in {1}'.format(key, q_sheet))
            else:
                values_list.append('%s="%s"' % (key, value))
        values = []
        sql_str += 'and'.join(values_list)
        try:
            self.cursor.execute(sql_str)
            values = self.cursor.fetchall()
        except BaseException as e:
            print('error: sql_str (%s)\n%s' % (sql_str,e))
        if len(values) == 0:
            return False
        fields = [i[0] for i in self.cursor.description]

        # zip_vals = [i.decode('utf-8') if isinstance(i, bytearray) else '%s' % i for i in values[0]]
        zip_vals = ['%s' % i for i in values[0]]
        return json.dumps(dict(zip(fields, zip_vals)))  # TODO:不考虑多条查询

    # TODO: 区别个别字段的状态范围0-4, 最好添加字段类型标准判断
    def insert_sheet_item(self, q_sheet, **kwargs):     # TODO: 可能误用导致重复导入多个
        """
        插入单个item
        :param q_sheet: 表名
        :param kwargs: 需要插入表的单个对象关键字段，必须传入所有必要字段
        :return: 成功时返回True，返回False时表名不存在、必要键值没有传入、或插入发生异常
        """
        if q_sheet not in DATA_SHEET:
            print('error: no sheet exist')
            return False
        for field in DATA_SHEET_FIELD_REQUIRED[q_sheet]:
            if field not in kwargs.keys():
                print('error: lost (%s)field value' % field)
                return False
        keys_list = DATA_SHEET_FIELD[q_sheet]
        # key_va_list = [item for item in keys_list if item not in ['reg_time', 'update_time']]
        values_list = []
        for field in keys_list:
            if field in kwargs.keys():
                field_val = kwargs[field]
                if isinstance(field_val, str):
                    field_val = kwargs[field].replace('"', '“')
                values_list.append('%s' % field_val)
            elif field in DATA_SHEET_TIME_REG + DATA_SHEET_TIME_UPDATA:
                values_list.append(datetime.now().strftime('%Y%m%d%H%M%S'))
            else:
                values_list.append('')
        sql_str = 'insert into %s (%s) values ("%s")' % (q_sheet,
                                                         ','.join(keys_list),
                                                         '","'.join(values_list))
        try:
            self.cursor.execute(sql_str)
            self.conn.commit()
        except BaseException as e:
            self.conn.rollback()
            print('error: sql_str(%s)\nexception:\n%s' % (sql_str, e))
            return False
        return True

    def update_sheet_item(self, q_sheet, key_field_val, **kwargs):
        """
        更新单个item
        :param q_sheet: 表名
        :param key_field_val: 主键值
        :param kwargs: 更新的字段
        :return: 成功时返回True，返回False时表名不存在、或更新发生异常
        """
        if q_sheet not in DATA_SHEET:
            print('error: no sheet exist')
            return False
        key_val_dict = {}
        key_field = DATA_SHEET_FIELD_KEY[q_sheet]
        for field in DATA_SHEET_FIELD[q_sheet].remove(key_field):
            if field in DATA_SHEET_TIME_UPDATA:
                key_val_dict[field] = datetime.now().strftime('%Y%m%d%H%M%S')
            elif field in kwargs.keys():
                field_val = kwargs[field]
                if isinstance(field_val, str):
                    field_val = kwargs[field].replace('"', '“')        # TODO:
                key_val_dict[field] = field_val
        set_list = ['%s="%s"' % (key, val) for key, val in key_val_dict]
        sql_str = 'update %s set %s where %s="%s"' % (q_sheet,
                                                      ','.join(set_list),
                                                      key_field,
                                                      key_field_val)
        try:
            self.cursor.execute(sql_str)
            self.conn.commit()
        except BaseException as e:
            self.conn.rollback()
            print('error: sql_str (%s)\nexception:\n%s' % (sql_str, e))
            return False
        return True

    def update_detail_task_id(self, task_id):
        """
        更新任务详细表
        :param task_id: 任务id
        :return: 返回False时任务id不存在，或更新发生异常
        """
        kwargs = {'task_id': task_id}
        values = self.query_sheet_item('tb_task_detail', **kwargs)
        if values:
            re_val = self.update_sheet_item('tb_task_detail', key_field_val=task_id, **{'status': 1})
            return json.dumps({'value': re_val})
        print('error: update fail')
        return json.dumps({'value': False})

    def update_result_task_id(self, task_id, status, result=''):
        """
        更新任务结果表
        :param task_id: 任务id
        :param status: 任务更新状态字段
        :param result: 更新结果字段
        :return: 返回False时任务id不存在，或更新发生异常
        """
        values = self.query_sheet_item('tb_task_result', **{'task_id': task_id})
        if values:  # TODO:
            kwargs = {'status': status}
            if result != '':
                kwargs['task_result'] = result
            re_val = self.update_sheet_item('tb_task_result', key_field_val=task_id, **kwargs)
            return json.dumps({'value': re_val})
        print('error: update fail')
        return json.dumps({'value': False})


if __name__ == '__main__':
    common = CommonModule()
    # common.update_detail_task_id('')
    # common.insert_sheet_item('tb_tg_account', **{'telnumber': '+8618888888888', 'appid': '2830580934',
    #                                              'secretkey': 'kjsoidjf', 'status': 0})
    val = common.query_sheet_item('tb_tg_account', **{'telnumber': '+8618888888888'})
    print(val)
