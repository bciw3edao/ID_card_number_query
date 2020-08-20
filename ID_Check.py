class ID_Check():
    # 錯誤提示和離開
    def Error_exit(self):
        print('輸入資料有誤，請重新輸入')
        return False
        exit()

    def checker(str_id):
        global code
        # 英文代號以下表轉換成數字
        code_list = [['A', '10', '台北市'], ['B', '11', '台中市'], ['C', '12', '基隆市'], ['D', '13', '台南市'],
                     ['E', '14', '高雄市'], ['F', '15', '台北縣'], ['G', '16', '宜蘭縣'], ['H', '17', '桃園縣'],
                     ['I', '34', '嘉義市'], ['J', '18', '新竹縣'], ['K', '19', '苗栗縣'], ['L', '20', '台中縣'],
                     ['M', '21', '南投縣'], ['N', '22', '彰化縣'], ['O', '35', '新竹市'], ['P', '23', '雲林縣'],
                     ['Q', '24', '嘉義縣'], ['R', '25', '台南縣'], ['S', '26', '高雄縣'], ['T', '27', '屏東縣'],
                     ['U', '28', '花蓮縣'], ['V', '29', '台東縣'], ['W', '32', '金門縣'], ['X', '30', '澎湖縣'],
                     ['Z', '33', '連江縣']]
        # 長度驗證
        if len(str_id) != 10:
            str_id.Error_exit()
        # 縣市驗證
        for code in range(len(code_list)):
            if str_id[0] == code_list[code][0]:
                print(code_list[code][2])
                break
        else:
            str_id.Error_exit()
        # 性別驗證
        if str_id[1] == '1' or 'A' or 'C':
            print('男性')
        elif str_id[1] == '2' or 'B' or 'D':
            print('女性')
        else:
            str_id.Error_exit()
        # 證號規則驗證
        All_id = code_list[code][1] + str_id[1:10]
        y = 0
        id_Weighted = '1987654321'
        for j in range(len(id_Weighted)):
            y += int(All_id[j]) * int(id_Weighted[j])
        if (10 - y % 10) == int(All_id[-1]):
            print('身份證字號驗證成功')
            return True
        else:
            str_id.Error_exit()

input_id='A123456789'
print(ID_Check.checker(input_id))