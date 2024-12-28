import customtkinter
import math
from fractions import Fraction

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("400x700")
        self.configure(fg_color="#faf5ef")
        
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        self.rowconfigure(8, weight=1)
        self.rowconfigure(9, weight=1)
        self.rowconfigure(10, weight=1)

        
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)
            


        # Display of Numbers
        self.display = customtkinter.CTkTextbox(self, width=350, height=120, border_width=2,bg_color="transparent",fg_color="#f1dec9" ,border_color="black", text_color="#8d7b68", font=("Helvetica", 30))
        self.display.place(relx=0.5, rely=0.12, anchor="center")
        

        # Number buttons
        self.zero_button = customtkinter.CTkButton(self, text="0", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#f1dec9", hover_color="#ffeedb", border_width=2, border_color="#f1dec9" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, 0))
        self.zero_button.grid(row=10, column=2)
        self.one_button = customtkinter.CTkButton(self, text="1", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#f1dec9", hover_color="#ffeedb", border_width=2, border_color="#f1dec9" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, 1))
        self.one_button.grid(row=9, column=2)
        self.two_button = customtkinter.CTkButton(self, text="2", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#f1dec9", hover_color="#ffeedb", border_width=2, border_color="#f1dec9" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, 2))
        self.two_button.grid(row=9, column=3)
        self.three_button = customtkinter.CTkButton(self, text="3", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#f1dec9", hover_color="#ffeedb", border_width=2, border_color="#f1dec9" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, 3))
        self.three_button.grid(row=9, column=4)
        self.four_button = customtkinter.CTkButton(self, text="4", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#f1dec9", hover_color="#ffeedb", border_width=2, border_color="#f1dec9" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, 4))
        self.four_button.grid(row=8, column=2)
        self.five_button = customtkinter.CTkButton(self, text="5", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#f1dec9", hover_color="#ffeedb", border_width=2, border_color="#f1dec9" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, 5))
        self.five_button.grid(row=8, column=3)
        self.six_button = customtkinter.CTkButton(self, text="6", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#f1dec9", hover_color="#ffeedb", border_width=2, border_color="#f1dec9" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, 6))
        self.six_button.grid(row=8, column=4)
        self.seven_button = customtkinter.CTkButton(self, text="7", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#f1dec9", hover_color="#ffeedb", border_width=2, border_color="#f1dec9" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, 7))
        self.seven_button.grid(row=7, column=2)
        self.eight_button = customtkinter.CTkButton(self, text="8", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#f1dec9", hover_color="#ffeedb", border_width=2, border_color="#f1dec9" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, 8))
        self.eight_button.grid(row=7, column=3)
        self.nine_button = customtkinter.CTkButton(self, text="9", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#f1dec9", hover_color="#ffeedb", border_width=2, border_color="#f1dec9" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, 9))
        self.nine_button.grid(row=7, column=4)
        
        
        # others
        self.decimal_button = customtkinter.CTkButton(self, text=".", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#f1dec9", hover_color="#ffeedb", border_width=2, border_color="#f1dec9" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, "."))
        self.decimal_button.grid(row=10, column=3)
        self.negative_button = customtkinter.CTkButton(self, text="(-)", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#f1dec9", hover_color="#ffeedb", border_width=2, border_color="#f1dec9" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, "-"))
        self.negative_button.grid(row=10, column=4)
        self.parenthese_open_button = customtkinter.CTkButton(self, text="(", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#c8b6a6", hover_color="#f1dec9", border_width=2, border_color="#c8b6a6" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, "("))
        self.parenthese_open_button.grid(row=6, column=3)
        self.parenthese_close_button = customtkinter.CTkButton(self, text=")", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#c8b6a6", hover_color="#f1dec9", border_width=2, border_color="#c8b6a6" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, ")"))
        self.parenthese_close_button.grid(row=6, column=4)
        self.e_button = customtkinter.CTkButton(self, text="e", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#c8b6a6", hover_color="#f1dec9", border_width=2, border_color="#c8b6a6" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, "e"))
        self.e_button.grid(row=7, column=1)
        

        # Operations
        self.add_button = customtkinter.CTkButton(self, text="+", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#d9b7a5", hover_color="#f7d1bc", border_width=2, border_color="#d9b7a5" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, "+"))
        self.add_button.grid(row=9, column=5)
        self.subtract_button = customtkinter.CTkButton(self, text="-", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#d9b7a5", hover_color="#f7d1bc", border_width=2, border_color="#d9b7a5" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, "-"))
        self.subtract_button.grid(row=8, column=5)
        self.multiply_button = customtkinter.CTkButton(self, text="×", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#d9b7a5", hover_color="#f7d1bc", border_width=2, border_color="#d9b7a5" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, "*"))
        self.multiply_button.grid(row=7, column=5)
        self.divide_button = customtkinter.CTkButton(self, text="÷", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#d9b7a5", hover_color="#f7d1bc", border_width=2, border_color="#d9b7a5" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, "/"))
        self.divide_button.grid(row=6, column=5)
        self.power_button = customtkinter.CTkButton(self, text="^", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#c8b6a6", hover_color="#f1dec9", border_width=2, border_color="#c8b6a6" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, "^"))
        self.power_button.grid(row=5, column=5)
        self.natural_log_button = customtkinter.CTkButton(self, text="ln", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#c8b6a6", hover_color="#f1dec9", border_width=2, border_color="#c8b6a6" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, "ln("))
        self.natural_log_button.grid(row=8, column=1)
        self.log_button = customtkinter.CTkButton(self, text="log", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#c8b6a6", hover_color="#f1dec9", border_width=2, border_color="#c8b6a6" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, "log("))
        self.log_button.grid(row=9, column=1)
        self.square_root_button = customtkinter.CTkButton(self, text="√", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#c8b6a6", hover_color="#f1dec9", border_width=2, border_color="#c8b6a6" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, "√"))
        self.square_root_button.grid(row=6, column=1)

        # Delete Button
        # end-2c is secomd to last character and 3nd-1c is last character
        self.clear_button = customtkinter.CTkButton(self, text="delete", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#c8b6a6", hover_color="#f1dec9", border_width=2, border_color="#c8b6a6" ,text_color="#8d7b68", command= lambda: self.display.delete("end-2c", "end-1c"))
        self.clear_button.grid(row=4, column=1)

        # Enter Button
        self.enter_button = customtkinter.CTkButton(self, text="enter", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#d9b7a5", hover_color="#f7d1bc", border_width=2, border_color="#d9b7a5" ,text_color="#8d7b68", command=self.evaluate)
        self.enter_button.grid(row=10, column=5)

        # Clear Button
        self.clear_button = customtkinter.CTkButton(self, text="clear", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#c8b6a6", hover_color="#f1dec9", border_width=2, border_color="#c8b6a6" ,text_color="#8d7b68", command= lambda: self.display.delete("0.0", customtkinter.END))
        self.clear_button.grid(row=4, column=5)

        # Fraction converter button
        self.fraction_button = customtkinter.CTkButton(self, text="frac", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#c8b6a6", hover_color="#f1dec9", border_width=2, border_color="#c8b6a6" ,text_color="#8d7b68", command=self.fraction_converter)
        self.fraction_button.grid(row=10, column=1)

        # Quad formula button
        self.quad_formula_button = customtkinter.CTkButton(self, text="Quad", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#c8b6a6", hover_color="#f1dec9", border_width=2, border_color="#c8b6a6" ,text_color="#8d7b68", command=self.quad_solver)                    
        self.quad_formula_button.grid(row=6, column=2)

        # Trig buttons
        self.sin_button = customtkinter.CTkButton(self, text="sin", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#c8b6a6", hover_color="#f1dec9", border_width=2, border_color="#c8b6a6" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, "sin("))
        self.sin_button.grid(row=5, column=2)
        self.cos_button = customtkinter.CTkButton(self, text="cos", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#c8b6a6", hover_color="#f1dec9", border_width=2, border_color="#c8b6a6" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, "cos("))
        self.cos_button.grid(row=5, column=3)
        self.tan_button = customtkinter.CTkButton(self, text="tan", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#c8b6a6", hover_color="#f1dec9", border_width=2, border_color="#c8b6a6" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, "tan("))
        self.tan_button.grid(row=5, column=4)
        self.pi_button = customtkinter.CTkButton(self, text="π", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#c8b6a6", hover_color="#f1dec9", border_width=2, border_color="#c8b6a6" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, "π"))
        self.pi_button.grid(row=5, column=1)

        self.sin_inverse_button = customtkinter.CTkButton(self, text="sin⁻¹", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#c8b6a6", hover_color="#f1dec9", border_width=2, border_color="#c8b6a6" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, "sin⁻¹("))
        self.sin_inverse_button.grid(row=4, column=2)
        self.cos_inverse_button = customtkinter.CTkButton(self, text="cos⁻¹", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#c8b6a6", hover_color="#f1dec9", border_width=2, border_color="#c8b6a6" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, "cos⁻¹("))
        self.cos_inverse_button.grid(row=4, column=3)
        self.tan_inverse_button = customtkinter.CTkButton(self, text="tan⁻¹", width=60, height=30, corner_radius=10, bg_color="transparent", fg_color="#c8b6a6", hover_color="#f1dec9", border_width=2, border_color="#c8b6a6" ,text_color="#8d7b68", command= lambda: self.display.insert(customtkinter.INSERT, "tan⁻¹("))
        self.tan_inverse_button.grid(row=4, column=4)
    

    def quad_solver(self):
        
        self.display.insert(customtkinter.INSERT, "Enter coeffeicients seperated by spaces 'a b c': \n")
        
        def solve():
            input = self.display.get("0.0", "end-1c")
            print(input)

            a = None
            b = None
            c = None

            var = input.split(" ")
            print(var)

            for i in var:
                try:
                    float(i)
                    if a == None:
                        a = float(i)
                        print(f"A: {a}")
                    elif b == None:
                        b = float(i)
                        print(f"B: {b}")
                    elif c == None:
                        c = float(i)
                        print(f"C: {c}")
                
                except ValueError:
                    pass

            self.display.delete("1.0", customtkinter.END)
            
            try:
                answer1 = str(round((-b+math.sqrt((b**2)-4*a*c))/(2*a), 10))
                print(answer1)
                
            except ValueError:
                if "math domain error":
                    answer1 = " "
                    print("whoops")
            
            try:
                answer2 = str(round((-b-math.sqrt((b**2)-4*a*c))/(2*a), 10))
                print(answer2)
                
            except ValueError:
                if "math domain error":
                    answer2 = " "
                    print("whoops")

            if answer1 == " " and answer2 == " ":
                self.display.insert(customtkinter.INSERT, "Non real numbers")
                self.enter_button.configure(text="enter", fg_color="#c8b6a6", hover_color="#f1dec9", border_color="#c8b6a6", command=self.evaluate)
                self.fraction_button.configure(self, text="frac", fg_color="#c8b6a6", hover_color="#f1dec9", border_color="#c8b6a6", command=self.fraction_converter)
            elif answer1 == " ":
                self.display.insert(customtkinter.INSERT, "x: " + answer2)
                self.enter_button.configure(text="enter", fg_color="#c8b6a6", hover_color="#f1dec9", border_color="#c8b6a6", command=self.evaluate)
                self.fraction_button.configure(self, text="frac", fg_color="#c8b6a6", hover_color="#f1dec9", border_color="#c8b6a6", command=self.fraction_converter)
            elif answer2 == " ":
                self.display.insert(customtkinter.INSERT, "x: " + answer1)
                self.enter_button.configure(text="enter", fg_color="#c8b6a6", hover_color="#f1dec9", border_color="#c8b6a6", command=self.evaluate)
                self.fraction_button.configure(self, text="frac", fg_color="#c8b6a6", hover_color="#f1dec9", border_color="#c8b6a6", command=self.fraction_converter)
            elif answer1 != " " and answer2 != " " and answer1 == answer2:
                self.display.insert(customtkinter.INSERT, "x: " + answer1)
                self.enter_button.configure(text="enter", fg_color="#c8b6a6", hover_color="#f1dec9", border_color="#c8b6a6", command=self.evaluate)
                self.fraction_button.configure(self, text="frac", fg_color="#c8b6a6", hover_color="#f1dec9", border_color="#c8b6a6", command=self.fraction_converter)
            else:
                self.display.insert(customtkinter.INSERT, "x: " + answer1 + ", " + answer2)
                self.enter_button.configure(text="enter", fg_color="#c8b6a6", hover_color="#f1dec9", border_color="#c8b6a6", command=self.evaluate)
                self.fraction_button.configure(self, text="frac", fg_color="#c8b6a6", hover_color="#f1dec9", border_color="#c8b6a6", command=self.fraction_converter)

        self.enter_button.configure(text="solve", fg_color="#D2BE76", hover_color="#E8DDB5", border_color="#D2BE76", command=solve)
        self.fraction_button.configure(text="space", fg_color="#D2BE76", hover_color= "#E8DDB5", border_color= "#D2BE76", command= lambda: self.display.insert(customtkinter.INSERT, " "))

    def fraction_converter(self):
        fraction_form = Fraction(self.display.get("0.0", "end-1c"))
        self.display.delete("1.0", customtkinter.END)   
        self.display.insert(customtkinter.INSERT, fraction_form)

    def evaluate(self):
        # gets the entered eqaution
        nums = self.display.get("0.0", customtkinter.END)
        print(nums)

        # make the problem answerable by the eval() built in function
        nums = nums.replace("^", "**")
        nums = nums.replace("sin(", "math.sin(")
        nums = nums.replace("cos(", "math.cos(")
        nums = nums.replace("tan(", "math.tan(")
        nums = nums.replace("log(", "math.log10(")
        nums = nums.replace("ln(", "math.log(")
        nums = nums.replace("π", "math.pi")
        nums = nums.replace("√", "math.sqrt(")
        nums = nums.replace("sin⁻¹(", "math.asin(")
        nums = nums.replace("cos⁻¹(", "math.acos(")
        nums = nums.replace("tan⁻¹(", "math.atan(")
        nums = nums.replace("e", "math.e")

        # runs through the equation and makes sure that we add "*" in places so the eval function operates correctly
        i = 0
        while i < len(nums)-1:
            # Adds * when a closed parenthesis is follwoed by a int
            if (nums[i] == ")" and nums[i+1].isdigit()):
                nums = nums[:i+1] + "*" + nums[i+1:]
                i+=1
            # is lower adds a * when we have a equation with cos(8cos(8. It checks if the equation has a lower case letter. Also makes sure that you can do cos(pi)
            if (nums[i].isdigit() or nums[i] == ")" or nums[i] == "(") and (nums[i+1] == "(" or nums[i+1].islower()) and nums[i-4:i] != "log1" and not (nums[i] == "(" and nums[i+1]=="m"):
                nums = nums[:i+1] + "*" + nums[i+1:]
                i+=1
            # if the chacrter before a number is a letter then add *
            if nums[i].isdigit() and nums[i-1].islower() and nums[i-3:i] != "log":
                nums = nums[:i] + "*" + nums[i:]
                i+=1
            i+=1

        # closes parenthesis if the user forgot
        open_parenthesis_counter = 0
        closed_parenthesis_counter = 0
        for i in range(len(nums)-1):
            if nums[i] == "(":
                open_parenthesis_counter += 1
            elif nums[i] == ")":
                closed_parenthesis_counter += 1
        nums += ")"*(open_parenthesis_counter - closed_parenthesis_counter)
           
        try:
            print(nums)
            answer = round(eval(nums), 10)
            print(answer)
            self.display.delete("0.0", customtkinter.END)
            self.display.insert(customtkinter.END, answer)

        except ValueError and TypeError and SyntaxError:
            self.display.delete("0.0", customtkinter.END)
            self.display.insert(customtkinter.INSERT, "Error")

        
     
        


if __name__ == "__main__":
    app = App()
    app.mainloop()