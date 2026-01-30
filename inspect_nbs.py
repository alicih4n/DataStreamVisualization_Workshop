import nbformat as nbf

def add_explanations(notebook_path, explanations):
    ntbk = nbf.read(notebook_path, nbf.NO_CONVERT)
    new_cells = []
    
    code_cell_index = 0
    
    for cell in ntbk.cells:
        if cell.cell_type == 'code':
            if code_cell_index < len(explanations):
                # explanation = explanations[code_cell_index]
                # new_cells.append(nbf.v4.new_markdown_cell(explanation))
                pass # Logic to match specific cells might be tricky blindly, 
                     # but typically we alternate or look for content.
                     # For this task, I'll rewrite the notebook content with injected cells manually
                     # by reading the current structure first.
            
            # Let's just create a new list of cells.
            pass
    
    # Since programmatically mapping explanations to existing cells blindly is risky, 
    # I will read the notebook content first to prepare the exact insertion.
    return ntbk

nb_EDA = nbf.read('notebooks/EDA.ipynb', nbf.NO_CONVERT)
print(f"EDA Cells: {len(nb_EDA.cells)}")
for i, cell in enumerate(nb_EDA.cells):
    print(f"Cell {i} ({cell.cell_type}): {cell.source[:50]}...")

nb_LR = nbf.read('notebooks/linear_regression.ipynb', nbf.NO_CONVERT)
print(f"LR Cells: {len(nb_LR.cells)}")
for i, cell in enumerate(nb_LR.cells):
    print(f"Cell {i} ({cell.cell_type}): {cell.source[:50]}...")
