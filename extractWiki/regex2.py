import re

folders = {
'AA',
'AB',
'AC',
'AD',
'AE',
'AF',
'AG',
'AH',
'AI',
'AJ',
'AK',
'AL',
'AM',
'AN',
'AO',
'AP',
'AQ',
'AR',
'AS',
'AT',
'AU',
'AV',
'AW',
'AX',
'AY',
'AZ',
'BA',
'BB',
'BC',
'BD',
'BE',
'BF',
'BG',
'BH',
'BI',
'BJ',
'BK',
'BL',
'BM',
'BN',
'BO',
'BP',
'BQ',
'BR',
'BS',
'BT',
'BU',
'BV',
'BW',
'BX',
'BY',
'BZ',
'CA',
'CB'
}

for folder in folders:
    infile = 'merged/'+folder+'/input.txt'
    outfile = 'bigWikiAllChars/'+folder+'/input.txt'
    with open(outfile, 'w') as f:
        f.write("")

    i = 0
    unique_chars = set()
    whitelist = set(' !"#\'(),-.0123456789:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÄäÖÜßöü\n')
    with open(infile,'r') as myfile:
        for line in myfile:
            i = i + 1
            line = re.sub(r'“', '"', line)
            line = re.sub(r'\\', '', line)
            line = re.sub(r'„', '"', line)
            line = re.sub(r'<[\S]*>', '', line)
            line = re.sub(r'<[\S, ]*>', '###', line)
            answer = ''
            for item in line:
                if item in whitelist:
                    answer = answer + item
                else:
                    answer = answer + '?'
            if len(answer) > 1:
                unique_chars = set(list(unique_chars) + list(set(answer)))
                with open(outfile, 'a') as f:
                    f.write(answer)
#print(sorted(unique_chars))
    unique_chars_text = ''.join(sorted(unique_chars))
#print('in set:',unique_chars_text)
    whitelist.add('\n')
    whitelist_text = ''.join(sorted(whitelist))
#print('whitelist:',whitelist_text)
    mybool = whitelist_text == unique_chars_text
    print('folder:', folder)
    print('all chars in set:', mybool)
