import networkx as nx
import matplotlib.pyplot as plt
import yfinance as yf

# define ticker
ticker_symbol = "QQQ"
stock = yf.Ticker(ticker_symbol)
# define timeframe of data
df = stock.history(period="8y")

df = df[['Open', 'Close']]
df["percent difference (day)"] = ((df["Close"] - df["Open"]) / df["Open"]) * 100
print(df.head())
percents = df["percent difference (day)"].to_list()


g = 0
r = 0
gg = 0
rr = 0
rg = 0
gr = 0
ggg = 0
ggr = 0
grg = 0
grr = 0
rrr = 0
rrg = 0
rgr = 0
rgg = 0
gggg = 0
gggr = 0
ggrg = 0
ggrr = 0
grrr = 0
grrg = 0
grgg = 0
grgr = 0
grgr = 0
grrr = 0
grrg = 0
rrrr = 0
rrrg = 0
rrgr = 0
rrgg = 0
rggg = 0
rggr = 0
rgrg = 0
rgrr = 0


for i in range(len(percents)-3):
    if float(percents[i]) >= 0:
        g +=1
        if float(percents[i+1]) >= 0:    
            gg +=1
            if float(percents[i+2]) >=0:
                ggg+=1
                if float(percents[i+3]) >=0:
                    gggg+=1
                else:
                    gggr+=1
            else:
                ggr+=1
                if float(percents[i+3]) >=0:
                    ggrg+=1
                else:
                    ggrr+=1
        else:
            gr+=1
            if float(percents[i+2]) >=0:
                grg+=1
                if float(percents[i+3]) >=0:
                    grgg+=1
                else:
                    grgr+=1
            else:
                grr+=1
                if float(percents[i+3]) >=0:
                    grrg+=1
                else:
                    grrr+=1

    else:
        r+=1
        if float(percents[i+1]) <= 0:
            rr+=1
            if float(percents[i+2]) >=0:
                rrg+=1
                if float(percents[i+3]) >=0:
                    rrgg+=1
                else:
                    rrgr+=1
            else:
                rrr+=1
                if float(percents[i+3]) >=0:
                    rrrg+=1
                else:
                    rrrr+=1
        else:
            rg+=1
            if float(percents[i+2]) >=0:
                rgg+=1
                if float(percents[i+3]) >=0:
                    rggg+=1
                else:
                    rggr+=1
            else:
                rgr+=1
                if float(percents[i+3]) >=0:
                    rgrg+=1
                else:
                    rgrr+=1


print(f"g: {g}  {g/len(percents)} check: {(g+r)/len(percents)}")
print(f"r: {r} {r/len(percents)} check: {(g+r)/len(percents)}")
print(f"gg: {gg} {gg/g} check: {(gg+gr)/g}")
print(f"gr: {gr} {gr/g} check: {(gg+gr)/g}")
print(f"rg: {rg} {rg/r} check: {(rg+rr)/r}")
print(f"rr: {rr} {rr/r} check: {(rg+rr)/r}")
print(f"ggg: {ggg} {ggg/gg} check: {(ggg+ggr)/gg}")
print(f"ggr: {ggr} {ggr/gg} check: {(ggg+ggr)/gg}")
print(f"grg: {grg} {grg/gr} check: {(grg+grr)/gr}")
print(f"grr: {grr} {grr/gr} check: {(grg+grr)/gr}")
print(f"rrr: {rrr} {rrr/rr} check: {(rrr+rrg)/rr}")
print(f"rrg: {rrg} {rrg/rr} check: {(rrr+rrg)/rr}")
print(f"rgr: {rgr} {rgr/rg} check: {(rgr+rgg)/rg}")
print(f"rgg: {rgg} {rgg/rg} check: {(rgr+rgg)/rg}")
print(f"gggg: {gggg} {gggg/ggg} check: {(gggg+gggr)/ggg}")
print(f"gggr: {gggr} {gggr/ggg} check: {(gggg+gggr)/ggg}")
print(f"ggrg: {ggrg} {ggrg/ggr} check: {(ggrg+ggrr)/ggr}")
print(f"ggrr: {ggrr} {ggrr/ggr} check: {(ggrg+ggrr)/ggr}")
print(f"grrr: {grrr} {grrr/grr} check: {(grrr+grrg)/grr}")
print(f"grrg: {grrg} {grrg/grr} check: {(grrr+grrg)/grr}")
print(f"grgg: {grgg} {grgg/grg} check: {(grgg+grgr)/grg}")
print(f"grgr: {grgr} {grgr/grg} check: {(grgg+grgr)/grg}")
print(f"rrrr: {rrrr} {rrrr/rrr} check: {(rrrr+rrrg)/rrr}")
print(f"rrrg: {rrrg} {rrrg/rrr} check: {(rrrr+rrrg)/rrr}")
print(f"rrgr: {rrgr} {rrgr/rrg} check: {(rrgr+rrgg)/rrg}")
print(f"rrgg: {rrgg} {rrgg/rrg} check: {(rrgr+rrgg)/rrg}")
print(f"rggg: {rggg} {rggg/rgg} check: {(rggg+rggr)/rgg}")
print(f"rggr: {rggr} {rggr/rgg} check: {(rggg+rggr)/rgg}")
print(f"rgrg: {rgrg} {rgrg/rgr} check: {(rgrg+rgrr)/rgr}")
print(f"rgrr: {rgrr} {rgrr/rgr} check: {(rgrg+rgrr)/rgr}")


print(f"days: {len(percents)}")


# Create a directed graph
G = nx.DiGraph()


# Define the tree structure with probabilities
tree_structure = {
    "Start": [("G", g/(g+r)), ("R", r/(g+r))],
    "G": [("GG", gg/g), ("GR", gr/g)],
    "R": [("RR", rr/r), ("RG", rg/r)],
    "GG": [("GGG", ggg/gg), ("GGR", ggr/gg)],
    "GR": [("GRG", grg/gr), ("GRR", grr/gr)],
    "RR": [("RRR", rrr/rr), ("RRG", rrg/rr)],
    "RG": [("RGR", rgr/rg), ("RGG", rgg/rg)],
    "GGG": [("GGGG", gggg/ggg), ("GGGR", gggr/ggg)],
    "GGR": [("GGRG", ggrg/ggr), ("GGRR", ggrr/ggr)],
    "GRG": [("GRGG", grgg/grg), ("GRGR", grgr/grg)],
    "GRR": [("GRRR", grrr/grr), ("GRRG", grrg/grr)],
    "RRR": [("RRRR", rrrr/rrr), ("RRRG", rrrg/rrr)],
    "RRG": [("RRGG", rrgg/rrg), ("RRGR", rrgr/rrg)],
    "RGR": [("RGRG", rgrg/rgr), ("RGRR", rgrr/rgr)],
    "RGG": [("RGGG", rggg/rgg), ("RGGR", rggr/rgg)]
}

# Add nodes and edges to the graph
for parent, children in tree_structure.items():
    for child, prob in children:
        G.add_edge(parent, child, weight=prob)

pos = nx.nx_agraph.graphviz_layout(G, prog="dot")

# Draw the graph
plt.figure(figsize=(12, 6))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold", edge_color="black")

# Draw edge labels with probabilities
edge_labels = {(u, v): f"{d['weight']:.4f}" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

# Display the plot
plt.title("Probability Tree Diagram")
plt.show()
