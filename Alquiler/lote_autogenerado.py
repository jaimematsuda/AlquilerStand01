#!/usr/bin/python
# -*- coding: UTF-8 -*-

import psycopg2
from datetime import datetime
#from dateutil.relativedelta import relativedelta

fecha = datetime.now()
dia = fecha.day
mes = fecha.month

if dia:
	print dia 
	print mes
	conxinfo = psycopg2.connect(
	    host='ec2-54-163-249-150.compute-1.amazonaws.com', 
	    user='aylgnbzzdmpfxx', 
	    password='R3ZifYzENKJSy_WBGMnd38yKjb', 
	    database='dbmsmd625mcd0s', 
	    #as_dict=True,
	    )

	curinfo = conxinfo.cursor()
	curinfo.execute('SELECT numero, inicio FROM lotes_lote ORDER BY id DESC \
					LIMIT 1')
	print type(curinfo)
	for row in curinfo:
		print row[0]
		print row[1]
		nuevolote = int(row[0]) + 1
		print nuevolote
	conxinfo.close()
	
"""
with open('/var/archivo/liquidacion/venezuela/%s.txt' % fecha, 'w') as archivo:

    archivo.write(fecha + '\t')

    '''
    DATOS DEL EFECTIVO SOLES Y DOLARES
    '''
    finicio = fecha + 'T08:00:00'
    fechasum = datetime.strptime(fecha, '%Y-%m-%d')
    fechasum = fechasum + relativedelta(days=1)
    f = str(fechasum)
    dia = f.split()
    ffinal = dia[0] + 'T07:59:59'
    tipopago = {'01': 'Nuevos Soles', '02': 'Dolares'}
    tipotarjeta = {'01': 'Visa', '02': 'Mastercard', '03': 'Dinners', \
        '04': 'Amex', '05': 'CMR Matercard', '06': 'Funo'}

    for clave, valor in sorted(tipopago.iteritems()):
        curinfo.execute('SELECT SUM(nmonto) FROM dpagodocumento WHERE \
            ttipopago=%(tipopago)s AND tmoneda=%(moneda)s AND fregistro BETWEEN \
            %(fechainicio)s AND %(fechafinal)s', {'tipopago': '01', 'moneda': clave,
            'fechainicio': finicio, 'fechafinal': ffinal})
        for row in curinfo:
            for val in row.itervalues():
                if clave == '01':
                    ventasoles = val
                if val > 0:
                    archivo.write('%.2f' % val + '\t')
                else:
                    archivo.write('%.2f' % 0.00 + '\t')

    curinfo.execute('SELECT TOP 1 ntipocambio FROM dpagodocumento WHERE fregistro \
        BETWEEN %(fechainicio)s AND %(fechafinal)s', {'fechainicio': finicio, \
        'fechafinal': ffinal})

    for row in curinfo:
        for valor in row.itervalues():
            tipocambio = float(valor)

    archivo.write('%.2f' % tipocambio + '\t')
    if val > 0:
        archivo.write('%.2f' % (tipocambio * float(val) + float(ventasoles)) + '\t')
    else:
        archivo.write('%.2f' % float(ventasoles) + '\t')

    '''
    PAGOS CON TARJETA
    '''
    for clave, valor in sorted(tipotarjeta.iteritems()):
        curinfo.execute('SELECT SUM(nmonto) FROM dpagodocumento WHERE \
            ttipopago=%(tipopago)s AND ttarjeta=%(tarjeta)s AND fregistro BETWEEN \
            %(fechainicio)s AND %(fechafinal)s', {'tipopago': '02', 'tarjeta': clave, \
            'fechainicio': finicio, 'fechafinal': ffinal})
        for row in curinfo:
            for val in row.itervalues():
                if clave == '01':
                    visa = val
                elif clave == '02':
                    mastercard = val
                elif clave == '03':
                    dinners = val
                elif clave == '04':
                    amex = val
                elif clave == '05':
                    cmr = val
                elif clave == '06':
                    funo = val

                if val > 0:
                    archivo.write('%.2f' % val + '\t')
                else:
                    archivo.write('%.2f' % 0.00 + '\t')

    '''
    EGRESOS
    '''
    curinfo.execute('SELECT tmoneda, ntipocambio, SUM(nmonto) monto FROM \
        megreso WHERE fregistro BETWEEN %(fechainicio)s AND %(fechafinal)s \
        GROUP BY tmoneda, ntipocambio',
        {'fechainicio': finicio, 'fechafinal': ffinal})

    for row in curinfo:
        if row['tmoneda'] == '01' and row['monto'] > 0:
            archivo.write('%.2f' % row['monto'] + '\t')
        else:
            archivo.write('%.2f' % 0.00 + '\t')
        if row['tmoneda'] == '02' and row['monto'] > 0:
            archivo.write('%.2f' % row['monto'] * row['ntipocambio'] + '\t')
        else:
            archivo.write('%.2f' % 0.00 + '\t')

    '''
    CORTESIAS
    '''
    curinfo.execute('SELECT SUM(nventa) cortesia FROM mdocumento WHERE \
        tcortesia<>%(cortesia)s AND fregistro BETWEEN %(fechainicio)s AND \
        %(fechafinal)s', {'cortesia': '', 'fechainicio': finicio, 'fechafinal': ffinal})

    for row in curinfo:
        if row['cortesia'] > 0:
            archivo.write('%.2f' % row['cortesia'] + '\t')
        else:
            archivo.write('%.2f' % 0.00 + '\t')

    '''
    CUENTAS CORRIENTES
    '''
    curinfo.execute('SELECT SUM(dp.nventa) FROM mpedido mp INNER JOIN \
        dpedido dp ON mp.tcodigopedido=dp.tcodigopedido WHERE \
        tclientectacte<>%(ctacte)s AND mp.fregistro BETWEEN %(fechainicio)s \
        AND %(fechafinal)s', {'ctacte': 'NULL', 'fechainicio': finicio, \
        'fechafinal': ffinal})
 
    for row in curinfo:
        x = row[0]
        if x == None:
            x = 0.00
            archivo.write('%.2f' % x + '\t')
        else:
            archivo.write('%.2f' % x + '\t')

conxinfo.close()
"""