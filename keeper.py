import gkeepapi
import yaml

class Keeper:
    keep = gkeepapi.Keep()
    email = ''
    password = ''
    token = ''

    def __init__(self):
        with open('config.yaml', 'r') as ymlfile:
            cfg = yaml.load(ymlfile)

        self.email = cfg['keep']['email']
        self.password = cfg['keep']['password']
        self.token = cfg['keep']['token']

        print('Email={}, Password={}, Token={}'.format(self.email, self.password, self.token))

        if self.token is None:
            print('Token not found in configuration proceed with normal login')
            self.keep.login(self.email, self.password)
            self.token = keep.getMasterToken()
        else:
            self.keep.resume(self.email, self.token)
        self.keep.sync()

    def resume(self, email, token):
        self.keep.resume(email, token)
        self.keep.sync()

    def login(self, email, password):
        self.keep.login(email, password)
        token = keep.getMasterToken()
        return token


    def getUncheckedItems(self, list_id):
        keepList = self.keep.get(list_id)
        unchecked = []
        for i in keepList.unchecked: 
            unchecked.append(i.text)
        return unchecked

    def getCheckedItems(self, list_id):
        keepList = self.keep.get(list_id)
        checked = []
        for i in keepList.checked: 
            checked.append(i.text)
        return checked

    def addItem(self, list_id, item):
        keepList = self.keep.get(list_id)
        keepList.add(item, False)
        self.keep.sync()

    def modifyCheckState(self, list_id, item):
        keepList = self.keep.get(list_id)
        for i in keepList.items:
            if i.text == item:
                i.checked = not i.checked
                break
        print('Done')
        self.keep.sync()