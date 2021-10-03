import zipfslaw

def main():

    try:

        f = open("greatgatsby.txt", "r")
        text = f.read()
        words = text.split()
        length = len(words)
        print('-----------------')
        print('|Zipfs Law                   |')
        print('|Total number of words: ' + str(length) + '|')
        print('-----------------\n')
        f.close()

        zipf_table = zipfslaw.generate_zipf_table(text, 50)

        zipfslaw.print_zipf_table(zipf_table)
        

    except IOError as e:

        print(e)
main()