"""
Scenario:
    - Your client has a subscription to a swing trading newsletter.
    - Every week the client gets an email with list of trades.
    - the client tracks their trades in a spreadsheet and every week they have to copy the
        trades from the email into their tracking spreadsheet.
    - The client wants a script that will parse the text from the email and create a csv
      so it is easy to copy all trades into the tracking list

Exercise
    * Create a program that will output a file with a list of trades listed in the email body.
    * The output file should have the following columns
    symbol,trade_type,entry_price,stop_loss_price,target_price

Hint/Suggestion:
    * first create a dictionary with all the trades. each trade is a dictionary and all dictionaries are in a list.
    * use the dictionary to create the file
"""

import pdb

inputPath = '.\example_email_1.txt'
outputPath = '.\output.cvs'

# # READ FILE and convert to DICTIONARY
def readFileToDictionary(inputPath):

    with open(inputPath, 'r') as file:
        textRead = file.read()

    listRead = textRead.split('\n\n')
    
    trades = []
    
    for trade in listRead:
        tradeSplit = trade.split()
        tradeDictionary = {
            'symbol': tradeSplit[0],
            'tradeType': tradeSplit[1],
            'entryPrice': tradeSplit[2],
            'stopLossPrice': tradeSplit[5],
            'targetPrice': tradeSplit[7]
        }
        trades.append(tradeDictionary)

    return trades

def createTradesFile(outputPath, trades):
    
    with open(outputPath, 'w') as file:
        file.write("symbol,tradeType,entryPrice,stopLossPrice,targetPrice\n\n")
        
        for i in trades:
            file.write(f"{i['symbol']},{i['tradeType']}, {i['entryPrice']}, {i['stopLossPrice']}, {i['targetPrice']}\n\n")

allTrades = readFileToDictionary(inputPath)

createTradesFile(outputPath, allTrades)