# 1.) Plot 1 Controls
def plot_one_controls(input, output, render, data, wrangle, pd, plt):
    @output
    @render.plot(alt="Line Plot")
    def elec_pop_graph():
        we_data = wrangle(data, pd, input.elec_pop_range()[0], input.elec_pop_range()[1])
        plt.title("World Electricity")
        plt.xlabel("Year")
        plt.ylabel("Electricity Generation (Terawatt Hours)")
        plt.grid(True)
        # plt.xticks(ticks = we_data['year'])
        plt.plot("year", "electricity_generation", data=we_data, linewidth=1, marker="o", markersize=4)

# 2.) Plot 2 Controls
def text_two_controls(input, output, render, data, wrangle):
    @output
    @render.text
    def sawce_text():
        sawce_data = wrangle(data=data, my_year=input.sawce_year())
        sawce_labels = sawce_data.index.values
        sawce_labels = sawce_labels[2:]
        # sawce_values = sawce_data.iloc[:,[0]]
        sawce_values = sawce_data.to_numpy()
        sawce_values = sawce_values[2:]
        sawce_values2 = []
        sx = []
        for x in sawce_values:
            for y in x:
                sawce_values2.append(y)
        for x in sawce_labels:
            x_new = x.split("_", 1)[0]
            x_new = x_new.capitalize()
            sx.append(x_new)
        # return type(sawce_values[0][0])
        return f"LABELS: {sawce_labels} + NEW LABELS: {sx}"

def plot_two_controls(input, output, render, data, wrangle, plt):
    @output
    @render.plot(alt="Pie Graph")
    def sawce_graph():
        sawce_data = wrangle(data=data, my_year=input.sawce_year())
        sawce_labels = sawce_data.index.values
        sawce_labels = sawce_labels[2:]
        # sawce_values = sawce_data.iloc[:,[0]]
        sawce_values = sawce_data.to_numpy()
        sawce_values = sawce_values[2:]
        sawce_values2 = []
        sx = []
        for x in sawce_values:
            for y in x:
                sawce_values2.append(y)
        for x in sawce_labels:
            x_new = x.split("_", 1)[0]
            x_new = x_new.capitalize()
            sx.append(x_new)
        plt.title("Distribution of Sources")
        plt.pie(sawce_values2, explode = (0.5,0,0,0,0,0,1.0,0.75), autopct='%1.1f%%', shadow = True, labeldistance = None, labels=sx)
        plt.axis('equal')
        plt.legend()


# 3.) Plot 3 Controls
def text_three_controls(input, output, render, data, wrangle, np, lm):
    @output
    @render.text
    def reg_sawce_text():
        reg_sawce_data = wrangle(data=data,my_country=input.reg_country(),sawce=input.reg_sawce_select(),year_range=[input.reg_year_range()[0], input.reg_year_range()[1]])
        rsd_na_filt = reg_sawce_data.iloc[:, [0, 1]].dropna()
        rgs_arr = np.array([rsd_na_filt.iloc[:, 0], rsd_na_filt.iloc[:, 1]])
        if rsd_na_filt.empty:
            return f"NO DATA FOUND"
        if reg_sawce_data.iloc[:, 0].isnull().values.any():
            lm.fit(rgs_arr[1, :].reshape(-1, 1), rgs_arr[0, :])
            return f"INCOMPLETE DATA\nR SQUARED: {lm.score(rgs_arr[1, :].reshape(-1, 1), rgs_arr[0, :])}"
        else:
            lm.fit(rgs_arr[1, :].reshape(-1, 1), rgs_arr[0, :])
            return f"R SQUARED: {lm.score(rgs_arr[1, :].reshape(-1, 1), rgs_arr[0, :])}"


def plot_three_controls(input, output, render, data, wrangle, np, lm, pm, plt):
    @output
    @render.plot(alt="Regression Plot")
    def reg_sawce_plot():
        reg_sawce_data = wrangle(data=data,my_country=input.reg_country(),sawce=input.reg_sawce_select(),year_range=[input.reg_year_range()[0], input.reg_year_range()[1]])
        rsd_na_filt = reg_sawce_data.iloc[:, [0, 1]].dropna()
        rgs_arr = np.array([rsd_na_filt.iloc[:, 0], rsd_na_filt.iloc[:, 1]])
        X, y = rgs_arr[1, :].reshape(-1, 1), rgs_arr[0, :]
        
        y_lm_pred = lm.intercept_ + (X) * lm.coef_

        if rsd_na_filt.empty:
            return
        if reg_sawce_data.iloc[:, 0].isnull().values.any():
            plt.xlabel("Year")
            plt.ylabel("Electricity Generation (Terawatt Hours)")
            plt.grid(True)
            plt.plot(list(X), list(y), linewidth=1, marker="o", markersize=4)
            if (input.reg_sawce_degree() == str(1)):
                lm.fit(X, y)
                plt.plot(list(X), y_lm_pred)
            elif(input.reg_sawce_degree() == str(2)):
                X_poly = pm.fit_transform(X)
                lm.fit(X_poly, y)
                y_pm_pred = lm.predict(X_poly)
                plt.plot(list(X), y_pm_pred)
        else:
            plt.xlabel("Year")
            plt.ylabel("Electricity Generation (Terawatt Hours)")
            plt.grid(True)
            plt.plot(list(X), list(y), linewidth=1, marker="o", markersize=4)
            if (input.reg_sawce_degree() == str(1)):
                lm.fit(X, y)
                plt.plot(list(X), y_lm_pred)
            elif(input.reg_sawce_degree() == str(2)):
                X_poly = pm.fit_transform(X)
                lm.fit(X_poly, y)
                y_pm_pred = lm.predict(X_poly)
                plt.plot(list(X), y_pm_pred)
            
