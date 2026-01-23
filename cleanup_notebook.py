import json

# Paths
input_nb_path = '/Users/alicihanozdemir/Documents/DataStreamVisualization_Workshop/DataStreamVisualization_Workshop.ipynb'
output_nb_path = input_nb_path # Overwrite directly

# Load the notebook
with open(input_nb_path, 'r') as f:
    nb = json.load(f)

# Helper function to check if a cell is an empty code cell or a placeholder
def is_empty_code_cell(cell):
    if cell['cell_type'] != 'code':
        return False
    source = "".join(cell.get('source', [])).strip()
    return source == ""

# Helper to remove duplicates: if we encounter two identical valid code cells, remove one.
# But more importantly, we want to remove the specific duplicate issue we saw:
# Cell 116 (null exec count) and Cell 136 (exec count 1) are identical "Step 1" code.
# Cell 191 (Step 2) and likely another copy.

# Strategy:
# 1. Create a signature for each cell (hash of source).
# 2. Iterate and keep only unique signatures IF they are code cells. Markdown cells can repeat? No, unlikely to want repeat MD.
# 3. Also filter out empty code cells.

unique_cells = []
seen_signatures = set()

# Special handling: We know exactly which "solution" blocks we wrote.
# We want to keep the "solution" blocks and REMOVE any previous attempts or duplicates.

for cell in nb['cells']:
    source = "".join(cell.get('source', []))
    signature = (cell['cell_type'], source)
    
    # Logic to remove empty code cells
    if is_empty_code_cell(cell):
        continue
    
    # Logic to remove duplicates
    if signature in seen_signatures:
        # It's a duplicate.
        # But wait, sometimes context matters. 
        # However, in this specific messed up file, the duplicates are adjacent or close.
        continue
    
    seen_signatures.add(signature)
    unique_cells.append(cell)

# Update notebook
nb['cells'] = unique_cells

with open(output_nb_path, 'w') as f:
    json.dump(nb, f, indent=1)

print("Cleaned up duplicates and empty cells.")
