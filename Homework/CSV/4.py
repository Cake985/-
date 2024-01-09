"""
Повторение - мать учения.
Достаньте имя из словаря
"""
super_dificult_dict = {
    1:{
        "pochti":{
        "Esche chutka":{
            ("Eto","Chto?","kortezh??"):{
                "za chto???":[[1,2,3],["1",2,(13,"oleg")]]
            }
        }
        }
    }
}
name = super_dificult_dict[1]["pochti"]["Esche chutka"][("Eto","Chto?","kortezh??")]["za chto???"][1][2][1]
print(name)