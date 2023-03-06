import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import random
from .subfunctions import calculate_weight, calc_PSI_param, SI_intsurf
from matplotlib.ticker import AutoMinorLocator
from matplotlib import gridspec

class exopsi:
    #Calculate Weight
    def calc_weight(self, ref_val, upper_lim, lower_lim, threshold=0.8):
        weight = list() 
        for i in range(0,len(ref_val)):
            weight.append(calculate_weight(ref_val[i], upper_lim[i], lower_lim[i], threshold))

        print(f"The calculated weight(s) is(are): {weight}")



    #Calculate PSI
    def calc_psi(self, params, upper_lims=None, lower_lims=None,ref_val=None,threshold = 0.8,int_param = None,surf_param = None,p_index = pd.Dataframe()):
        colnames = list(params.columns)
    
        #Default Upper Lims
        if upper_lims is None:
            upper_lims = [float("NaN")]*len(colnames)

        #Default Lower Lims 
        if lower_lims is None:
            lower_lims = [float("NaN")]*len(colnames)
    
        if ref_val is None:
            ref_val = [float("NaN")]*len(colnames)
            
        try:
            #Perform sanity checks 
            len(colnames) == len(upper_lims) == len(lower_lims) == len(ref_val)
            
            for i in range(0, len(upper_lims)):
                upper_lims[i]>=lower_lims[i]

            #Calculate Weights    
            PSI_df = pd.DataFrame()
            for i in range(0, len(colnames)):
                PSI_param = calc_PSI_param(params.iloc[:,[i]], upper_lims[i], lower_lims[i],ref_val[i],threshold)
                PSI_colname = "PSI_{}".format(colnames[i])
                PSI_df[PSI_colname] = PSI_param
            PSI_df.index = params.index
            if int_param != None:
                PSI_int_param = list('PSI_{}'.format(col) for col in int_param)
                PSI_df['PSI_Interior'] = SI_intsurf(PSI_df.loc[:,PSI_int_param])
            if surf_param != None:
                PSI_surf_param = list('PSI_{}'.format(col) for col in surf_param)
                PSI_df['PSI_Surface'] = SI_intsurf(PSI_df.loc[:,PSI_surf_param])
            if int_param != None and surf_param != None:
                PSI_df['PSI_Global'] = SI_intsurf(PSI_df.loc[:,['PSI_Interior','PSI_Surface']])
            if p_index.empty != True:
                PSI_df.insert(loc = 0, column = 'P.Name', value = p_index)
            
            return PSI_df
            
        
        
        except ValueError as e:
            print(e)




    #PLOTTING FUNCTIONS
    #1.Plot Interior vs Surface PSI
    def psi_scale(self, df, x=None, y=None):

        if (x==None and y==None):  
            #sample = random.sample(sorted(df['PSI_Global']),200)
            data_x = df['PSI_Interior']
            data_y = df['PSI_Surface']
        else:
            data_x = df[x]
            data_y = df[y]
        
        fig,ax = plt.subplots(1)
        scatter = ax.scatter(data_x, data_y, cmap="viridis")
        plt.xlabel("PSI_Interior")
        plt.ylabel("PSI_Surface")
        plt.title("PSI Scale")
        
        #Create Annotation Object
        annotation = ax.annotate(
            text='',
            xy=(0, 0),
            xytext=(15, 15), # distance from x, y
            textcoords='offset points',
            bbox={'boxstyle': 'round', 'fc': 'w'},
            arrowprops={'arrowstyle': '->'}
        )
        annotation.set_visible(False)


        def mouse_hover(event):
            annotation_visbility = annotation.get_visible()
            if event.inaxes == ax:
                is_contained, annotation_index = scatter.contains(event)

                if is_contained:
                    data_point_location = scatter.get_offsets()[annotation_index['ind'][0]]
                    data_point_index = df.index[(df['PSI_Interior'] == data_point_location[0]) & (df['PSI_Surface'] == data_point_location[1])]
                    data_point_row = df.loc[data_point_index]

                    planet_name = data_point_row['P.Name'].values[0]
                    annotation.xy = data_point_location
                    

                    xlabel = planet_name
                    #ylabel = round(data_point_location[1],2)
                    text_label = f"{xlabel}"
                
                    #text_label = '({0:.2f}, {0:.2f})'.format(data_point_location[0], data_point_location[1])
                    annotation.set_text(text_label)
                    annotation.set_visible(True)
                    fig.canvas.draw_idle()
                    
                else:
                    if annotation_visbility:
                        annotation.set_visible(False)
                        fig.canvas.draw_idle()


        fig.canvas.mpl_connect('motion_notify_event', mouse_hover)
        plt.show()
        return fig 

    #Plot 2: Planetary bodies histogram
    def psi_dist(self, df):

        facecolor = '#EAEAEA'
        color_bars = '#3475D0'
        txt_color1 = '#252525'
        txt_color2 = '#004C74'

        # df['bin'] = pd.cut(df['PSI_Global'], [0,0.2,0.4,0.6,0.8,1.0], labels=['0-0.2','0.2-0.4', '0.4-0.6', '0.6-0.8', '0.8-1.0'])
        # imd = df.groupby(['bin']).count()
        # y = imd['PSI_Global']
    
        # plot
        fig, ax = plt.subplots(facecolor=facecolor, figsize=(8,4))
        ax.set_facecolor(facecolor)
        n, bins, patches = ax.hist(df['PSI_Global'], bins=[0,0.2,0.4,0.6,0.8,1.0], color=color_bars)


        minor_locator = AutoMinorLocator(2)
        plt.gca().xaxis.set_minor_locator(minor_locator)
        plt.grid(which='minor', lw = 2.0, color=facecolor)

        # x ticks labels
        #x_tickslabels = [ "{:.2f} - {:.2f}".format(value, bins[idx+1]) for idx, value in enumerate(bins[:-1])]
        x_tickslabels = ["Very Low Similarity", "Low Similarity", "Moderate Similarity","High Similarity", "Very High Similarity"]
        # x ticks positions
        x_ticks = [(bins[idx+1] + value)/2 for idx, value in enumerate(bins[:-1])]

        plt.xticks(x_ticks, labels = x_tickslabels, c=txt_color1, fontsize=10)
        


        plt.xlabel('\nPSI Values', c=txt_color2, fontsize=10)
        plt.ylabel('No. of Planets', c=txt_color2, fontsize=10)
        plt.tight_layout()
        plt.title('PSI Distribution', loc = 'center', fontsize = 12)
    
        # remove major and minor ticks from the x axis, but keep the labels
        ax.tick_params(axis='x', which='both',length=0)
        # Hide the right and top spines
        # remove major and minor ticks from the x axis, but keep the labels
        ax.tick_params(axis='x', which='both',length=0)
        
        # remove y ticks
        plt.yticks([])


        # Hide the right and top spines
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)

        # plot values on top of bars
        for idx, value in enumerate(n):
            if value > 0:
                plt.text(x_ticks[idx], value+5, int(value),ha='center', fontsize=8, c=txt_color1)
                
        plt.show()
        return fig 

    #function to convert units of P1 wrt P2, all columns should have same units
    def unit_conv(self, data,ref_index,unit_name, p_index = pd.DataFrame()):
        unit_conv_df = pd.DataFrame() 
        for j in data.index:
            k=0 
            for i in data.columns:
                x = float(data.loc[j,i])/ref_index[k]
                unit_conv_colname = "{} in {}".format(i,unit_name)
                unit_conv_df.loc[j,unit_conv_colname] = x
                k+=1
        if p_index.empty != True:
            unit_conv_df.index = p_index        
        return unit_conv_df