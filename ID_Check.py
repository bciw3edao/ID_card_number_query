class ID_Check:

    def checker(self):
        Counties_code = ()  # 縣市代碼
        place_of_birth = str()  # 出生地
        sex = str()  # 性別
        # 英文代號以下表轉換成數字
        code_list = [['A', '10', '台北市'], ['B', '11', '台中市'], ['C', '12', '基隆市'], ['D', '13', '台南市'],
                     ['E', '14', '高雄市'], ['F', '15', '台北縣'], ['G', '16', '宜蘭縣'], ['H', '17', '桃園縣'],
                     ['I', '34', '嘉義市'], ['J', '18', '新竹縣'], ['K', '19', '苗栗縣'], ['L', '20', '台中縣'],
                     ['M', '21', '南投縣'], ['N', '22', '彰化縣'], ['O', '35', '新竹市'], ['P', '23', '雲林縣'],
                     ['Q', '24', '嘉義縣'], ['R', '25', '台南縣'], ['S', '26', '高雄縣'], ['T', '27', '屏東縣'],
                     ['U', '28', '花蓮縣'], ['V', '29', '台東縣'], ['W', '32', '金門縣'], ['X', '30', '澎湖縣'],
                     ['Z', '33', '連江縣']]
        # 大小寫轉換
        self = self.upper()
        # 數字驗證
        if not self[1:].isnumeric():
            return False
        # 長度驗證
        if len(self) != 10:
            return False
        # 縣市驗證
        for code in range(len(code_list)):
            if self[0] == code_list[code][0]:
                place_of_birth = code_list[code][2]
                Counties_code = code_list[code][1]
                break
        else:
            return False
        # 性別驗證
        if self[1] == '1':
            sex = '男性'
        elif self[1] == '2':
            sex = '女性'
        else:
            return False
        # 證號規則驗證
        All_id = Counties_code + ('1' if sex == '男性' else '2') + self[2:10]  # 原始數據
        all_Weighted = 0  # 總加權預設
        id_Weighted = '1987654321'  # 個別加權設定
        # 進行個別加權
        for j in range(len(id_Weighted)):
            all_Weighted += int(All_id[j]) * int(id_Weighted[j])
        # 總加權驗證
        if (10 - all_Weighted % 10) == int(All_id[-1]):
            # print('身份證字號驗證成功')
            return True, place_of_birth, sex
        else:
            return False


input_id = 'AA23456789'
print(type(ID_Check.checker(input_id)))
print(ID_Check.checker(input_id))
# print(not input_id[2:].isnumeric())
