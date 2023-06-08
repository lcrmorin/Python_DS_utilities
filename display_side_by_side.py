import pandas as pd 

# Display dataframe stlyes side by side
def display_sbs(df_list, title_list):
    html = [df.set_table_attributes("style='display:inline'")
            .set_caption(title)._repr_html_() 
            for df, title in zip(df_list,title_list)]
    
    display_html("\xa0\xa0\xa0".join(html), raw=True)
