from prettytable import PrettyTable

text = 'Мистер и миссис Дурсль проживали в доме номер четыре по Тисовой улице и всегда с гордостью заявляли, что они, слава богу, абсолютно нормальные люди. Уж от кого-кого, а от них никак нельзя было ожидать, чтобы они попали в какую-нибудь странную или загадочную ситуацию.'
table = PrettyTable(["1", "2", "3", "4"])

td_data = text.split(' ') + (4 - (len(text.split(' ')) % 4)) * ['']
while td_data:
    table.add_row(td_data[:4])
    td_data = td_data[4:]

print(table)
