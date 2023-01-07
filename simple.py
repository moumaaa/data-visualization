import pandas as pd
import plotly as plt

pd.options.plotting.backend = "plotly"

df = pd.DataFrame(dict(a=[5,10,15, 20], b=[20,40,60, 80]))
fig = df.plot(title="Simple Example",
              labels=dict(index="X-Axis", value="Y-Axis", variable="Legend"))
fig.show()
