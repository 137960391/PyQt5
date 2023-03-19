import configparser


class UiTable:
    title_row = []
    title_col = []
    sale_money = []
    head = ''

    def __init__(self, datatime, sale_money_text):
        # self.head = '天猫2月28销售明细  /22年2月销售总额299,027'
        self.title_col = []
        self.title_row = ['产品', '销量', '销量占比', '销售额', '销售额占比']
        # self.title_col = ['产品', '其他文具', '国产相册', '本册', '碎纸机', '进口相册', '白板笔类', '墨水', '汇总', '当月累计']
        self.data_init(datatime)
        self.update_head(datatime, sale_money_text)

    def data_init(self, data):
        config = configparser.ConfigParser()
        config.read('../../config.ini')
        for key in config['title_col']:
            self.title_col.append(config['title_col'][key])
        for key in config['sale_money']:
            self.sale_money.append(config['sale_money'][key])

    def update_head(self, current_date, sale_money_text):
        # Get the current month and year
        curr_month = int(current_date[5:7])
        curr_year = int(current_date[2:4])
        # Get the sales money text for the given month
        # Construct the updated string with sales money text
        self.head = f'天猫{curr_month}月{current_date[-2:]}销售明细  /{curr_year}年{curr_month}月销售总额{sale_money_text}'

    def m_print(self):
        print(self.title_col)
        print(self.head)


# UiTable().m_print()





