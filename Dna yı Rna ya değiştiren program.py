def DNA_RNA_Donustur(dnaString):
    rnaString=""
    for i in dnaString:
        if i=='A':
            rnaString=rnaString+'U'
        elif i=='C':
            rnaString=rnaString+'G'
        elif i=='G':
            rnaString=rnaString+'C'
        elif i=='T':
            rnaString=rnaString+'A'
    print("RNA karsiligi : ",rnaString)
    
def main():
    
    dna=(input("Bir DNA dizilimi giriniz :"))
    
    while dna !="-1":
        DNA_RNA_Donustur(dna)
        dna=(input("Bir DNA dizilimi giriniz:"))
        
    print("Program sonlandi !")
    
main()    