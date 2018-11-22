"""sqlalchemy  ORM 对象-关系映射
"""
from os.path import dirname
from sqlalchemy import Column, String, Integer, create_engine, orm, exc, desc
from sqlalchemy.ext.declarative import declarative_base
from password import user, mysql_passwd
# 对象基类,可以自动与一表关联
base = declarative_base()
# 数据库类型+数据库驱动://用户名:密码（没有密码则为空，不填）@数据库主机地址/数据库名?编码
# dialect+driver://username:password@host:port/database?charset=utf8mb4
dbname = 'ex1'
DSN = f'mysql+pymysql://{user}:{mysql_passwd}@localhost:3306/{dbname}'
# User对象


def tformat(s): return str(s).title().ljust(10)


class Employee(base):

    #  该表在数据库中的名字
    __tablename__ = 'Employee'
    # 结构
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    age = Column(Integer)
    time = Column(Integer)

    def __str__(self):
        return ''.join(map(tformat, (self.id, self.name, self.age, self.time)))


class EmployeeOperation(object):

    def __init__(self, dsn):
        try:
            # 初始化数据库连接，可直接与数据库交互，或传递给一个Session,echo查看生成的sql语句
            eng = create_engine(dsn, echo=True)
            # 引擎创建失败，不支持所选的数据库，通常抛出ImportError
        except ImportError:
            raise RuntimeError()
        # 连接数据库
        try:
            eng.connect()
        # 连接不上，不存在，则创建该库，重新连接
        except exc.OperationalError:
            eng = create_engine(dirname(dsn))
            connection = eng.connect()
            connection.execute(f'CREATE DATABASE {dbname}').close()
            eng = create_engine(dsn)
        # 创建数据库会话类
        Session = orm.sessionmaker(bind=eng)
        # 用这个类实例化 一个数据库连接
        self.ses = Session()
        self.users = Employee.__table__
        # 引擎和表的元数据进行额外的绑定，这张表的所有操作都会绑定到这个指定的引擎中，
        self.eng = self.users.metadata.bind = eng

    def insert(self, **dit_args):

        self.ses.add(Employee(id=dit_args['id'], name=dit_args['name'],
                              age=dit_args['age'], time=dit_args['time']
                              ))
        self.ses.commit()
    # def insert(self):
    #     self.ses.add(Employee(id=9, name='kk', age=22, time=222))
    #     self.ses.commit()

    def get_all(self):
        # printf('\n%s' % ''.join(map(cformat,FIELDS)))
        users = self.ses.query(Employee).order_by(desc(Employee.id)).all()
        for user in users:
            print(user)
        self.ses.commit()

    def delete(self, user_id):
        # filter_by 返回查询结果集
        # user = self.ses.query(Employee).filter_by(id=user_id).first()
        user = self.ses.query(Employee).filter(Employee.id == user_id).first()
        self.ses.delete(user)
        self.ses.commit()
    # 委托

    def __getattr__(self, attr):
        return getattr(self.users, attr)

    # 关闭session
    def finish(self):
        self.ses.connection().close()


def main():
    try:
        orm = EmployeeOperation(DSN)
    except RuntimeError:
        print('Error:not supported\n')
        return
    Uly = {'id': 10, 'name': 'Ulysess', 'age': 22, 'time': 222}
    if orm.exists():
        orm.drop()
    orm.create()
    orm.insert(**Uly)
    # orm.delete(22)
    orm.get_all()
    orm.finish()


if __name__ == "__main__":
    print(DSN)
    main()
