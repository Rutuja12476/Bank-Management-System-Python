class BankAccount:
    def __init__(self, acc_no,name,  balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    
    def save_to_file(self):
        with open("ba1.txt", "a") as f:
            f.write(str(self.acc_no) + "," +
                    self.name + "," +
               str(self.balance) + "\n")
    @staticmethod   
    def create_account():
        acc_no=input("Enter Account Number:")
        with open("ba1.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == acc_no:
                    print("❌ Account Number Already Exists!")
                    return
        name=input("Enter Name:")
        balance=float(input("Enter Balance:"))
        print("Account Created Successfully ✅")

        ba=BankAccount(acc_no,name,balance)
        ba.save_to_file()
    @staticmethod
    def deposit():
        acc_no=input("Enter Account Number:")
        

        lines=[]

        with open("ba1.txt","r") as f:
            lines=f.readlines()

        found=False

        
        
        with open("ba1.txt","w") as f:
            for line in lines:
                data=line.strip().split(",")

                if data[0]==acc_no:
                    found=True
                    amount=float(input("Enter Amount To Deposit:"))
                    data[2]=str(float(data[2])+amount)   
                    print(amount, "Amount Deposited Successfully ✅")
                    print("Total Balance:", data[2])
                
                f.write(",".join(data)+"\n")

        if not found:
            print("❌ Account Not Found")
            print("Please Create Your Account First")

    @staticmethod
    def withdraw():
        acc_no=input("Enter Account Number:")
        

        found=False

        with open("ba1.txt","r") as f:
            lines=f.readlines()

            with open("ba1.txt","w") as f:
                for line in lines:
                    data=line.strip().split(",")

                    if data[0]==acc_no:
                        found=True
                        amount=float(input("Enter Amount For Withdraw:"))

                        balance=float(data[2])
                        
                        if amount<=balance:
                            balance-=amount
                            data[2]=str(balance)
                            print(amount, "Rs Withdrawn Successfully ✅")
                            print("Remaining Balance:", data[2])
                        else:
                             print("❌ Insufficient Balance")

                    f.write(",".join(data)+"\n")

            if not found:
                print("❌ Account Not Found")
                print("Please Create Your Account First")
    @staticmethod
    def display_account():
        acc_no=input("Enter Account Number That You Want To Get Details:")
      
        with open("ba1.txt","r") as f:
            for line in f:
                data=line.strip().split(",")
            
                if data[0]==acc_no:
                    print("\nAccount Details")
                    print("Account No:", data[0])
                    print("Name:", data[1])
                    print("Balance:", data[2])

                    return
            print("❌ Account Not Found")
    
    @staticmethod
    def delete_account():
        acc_no = input("Enter Account Number To Delete: ")

        found = False

        with open("ba1.txt", "r") as f:
            lines = f.readlines()

        with open("ba1.txt", "w") as f:
            for line in lines:
                data = line.strip().split(",")

                if data[0] == acc_no:
                    found = True
                    continue  

                f.write(line)

        if found:
            print(" Account Deleted Successfully")
        else:
            print("❌ Account Not Found")



while True:
    print("\n🏦 ===== BANK MANAGEMENT SYSTEM ===== 🏦")
    print("1. 👤 Create Account")
    print("2. 💰 Deposit Money")
    print("3. 💸 Withdraw Money")
    print("4. 📄 Display Account")
    print("5. ❎ Delete Account")
    print("6. 🚪 Exit")
   

    choice = int(input("Enter Choice: "))

    if choice == 1:
        BankAccount.create_account()
    
    elif choice==2:
        BankAccount.deposit()

    elif choice==3:
        BankAccount.withdraw()

    elif choice==4:
        BankAccount.display_account()
    
    elif choice==5:
        BankAccount.delete_account()
    
    elif choice==6:
        print("🙏 Thank You For Using Bank Management System")
        break
        
    else:
        print("Invalid Choice")
       
       

       
