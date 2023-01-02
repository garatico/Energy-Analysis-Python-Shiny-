######### CONTAINS OLD USED FOR TESTING / NOTES #########
######### DEFINITIONS #########
# loc = Filtering based on normal criterion
# iloc = Filtering based on indexes
# df.T = Transposes the dataframe

######### CONCEPTS #########
# First Class Functions = Ability to treat functions as variables. 
# Closure = 
# Decorator = 

######### COMMANDS #########
# RUN APP COMMAND:
# $ shiny run --reload app.py


######### OLD CODE #########
'''
    @output 
    @render.text
    def elec_pop_year_range():
        return f"Range is from {input.elec_pop_range()[0]} to {input.elec_pop_range()[1]}"
'''

'''
@output
    @render.text
    def sawce_text():
        sawce_data = sawces_my_year_data(data = e_data, my_year = input.sawce_year())
        sawce_labels = sawce_data.index.values
        sawce_labels = sawce_labels[2:]
        #sawce_values = sawce_data.iloc[:,[0]]
        sawce_values = sawce_data.to_numpy()
        sawce_values = sawce_values[2:]
        sawce_values2 = []
        for x in sawce_values:
            for y in x:
                sawce_values2.append(y)
        #return type(sawce_values[0][0])
        return f'{len(sawce_values2)} LABELS: {len(sawce_labels)}'


'''




