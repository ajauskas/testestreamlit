import streamlit as st
import pandas as pd
#import folium
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models
import biogeme.version as ver
from biogeme.expressions import Beta

st.write("""
# Biogeme app - by VTM
Utilize o exemplo do *Swissmetro* ou faça o upload de sua base de dados
""")

import streamlit as st
import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models
import biogeme.version as ver
from biogeme.expressions import Beta

file = "swissmetro.dat"

uploaded_file = st.file_uploader("Upload .dat", type=".dat")

use_example_file = st.checkbox(
    "Use example file", True, help="Use in-built example file to demo the app"
)

# If CSV is not uploaded and checkbox is filled, use values from the example file
# and pass them down to the next if block
if use_example_file:
    uploaded_file = file

df = pd.read_csv(uploaded_file, sep='\t')
print(df)
df.describe()

database = db.Database("swissmetro",df)
globals().update(database.variables)

ver.getVersion()

database.getSampleSize()
exclude = (( PURPOSE != 1 ) * (  PURPOSE   !=  3  ) +  ( CHOICE == 0 )) > 0
database.remove(exclude)
database.getSampleSize()

ASC_CAR = Beta('ASC_CAR', 0, None, None, 0)
ASC_TRAIN = Beta('ASC_TRAIN', 0, None, None, 0)
ASC_SM = Beta('ASC_SM', 0, None, None, 1)
B_TIME = Beta('B_TIME', 0, None, None, 0)
B_COST = Beta('B_COST', 0, None, None, 0)

SM_COST = SM_CO * (GA == 0)
TRAIN_COST = TRAIN_CO * (GA == 0)
CAR_AV_SP = CAR_AV * (SP != 0)
TRAIN_AV_SP = TRAIN_AV * (SP != 0)
TRAIN_TT_SCALED = TRAIN_TT / 100
TRAIN_COST_SCALED = TRAIN_COST / 100
SM_TT_SCALED = SM_TT / 100
SM_COST_SCALED = SM_COST / 100
CAR_TT_SCALED = CAR_TT / 100
CAR_CO_SCALED = CAR_CO / 100


V1 = ASC_TRAIN + \
     B_TIME * TRAIN_TT_SCALED + \
     B_COST * TRAIN_COST_SCALED
V2 = ASC_SM + \
     B_TIME * SM_TT_SCALED + \
     B_COST * SM_COST_SCALED
V3 = ASC_CAR + \
     B_TIME * CAR_TT_SCALED + \
     B_COST * CAR_CO_SCALED

V1
V2
V3

#V1 = st.chat_input("Definir V1")
#V2 = st.chat_input("Definir V2")
#V3 = st.chat_input("Definir V3")

V = {1: V1,
     2: V2,
     3: V3}

av = {1: TRAIN_AV_SP,
      2: SM_AV,
      3: CAR_AV_SP}

logprob = models.loglogit(V, av, CHOICE)

biogeme = bio.BIOGEME(database, logprob)
biogeme.modelName = '01logit'
results = biogeme.estimate()
pandasResults = results.getEstimatedParameters()
pandasResults
print(results)
