def extract_month(str_fecha):
    months = {
        '01': 'Enero',
        '02': 'Febrero',
        '03': 'Marzo',
        '04': 'Abril',
        '05': 'Mayo',
        '06': 'Junio',
        '07': 'Julio',
        '08': 'Agosto',
        '09': 'Septiembre',
        '10': 'Octubre',
        '11': 'Noviembre',
        '12': 'Diciembre'
    }

    return months[str_fecha[:2]]

def extract_year(str_short_date):
    years = {}
    for i in range(10, 100, 1):
        years[i] = '20' + str(i)

    return years[int(str_short_date[2:])]

print('{0} de {1}'.format(extract_month('0117'),extract_year('0117')))