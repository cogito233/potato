"""
Table Layout
"""

def generate_table_layout(annotation_scheme):

    schematic = (
        '<form action="/action_page.php">'
        + "  <fieldset>"
        + (
            '  <legend>%s</legend>'
            % annotation_scheme["description"]
        )
    )
    name = annotation_scheme["name"]
    schematic += '<table id="dynamicTable_' + name + '">'

    # Create the table headers
    schematic += '<tr>'
    schematic += '<th style="color:black;">#</th>'  # 第0列的表头
    for label in annotation_scheme["labels"]:
        schematic += '<th style="color:black;">{}</th>'.format(label)
    schematic += '</tr>'

    # Process label widths
    if "label_width" in annotation_scheme:
        widths = annotation_scheme["label_width"]
    else:
        widths = [5] * len(annotation_scheme["labels"])  # default width if not provided

    # Determine the number of rows
    row_count = annotation_scheme.get("rows", 5)

    # Generate table rows
    for row_num in range(1, row_count + 1):
        schematic += '<tr>'
        schematic += '<td style="color:black;">{}</td>'.format(row_num)  # 显示行号
        for idx, label in enumerate(annotation_scheme["labels"]):
            name = "{}:::{}_{}".format(annotation_scheme["name"], label.replace(" ", "_"), row_num)
            
            if annotation_scheme["type"][idx] == "text":
                schematic += (
                    '<td><textarea rows="1" cols="{}" class="{}" type="text" id="{}" name="{}" validation=""></textarea></td>'
                ).format(widths[idx], annotation_scheme["name"], name, name)
            
            else:
                raise NotImplementedError
                # annotation_scheme["type"][idx] == "multiselect":
                # options = annotation_scheme["select_option"].get(label, [])
                # schematic += '<td><select size="1" class="{}" name="{}">'.format(annotation_scheme["name"], name)
                # for option in options:
                #     schematic += '<option value="{}">{}</option>'.format(option, option)
                # schematic += '</select></td>'
                
        schematic += '</tr>'

    # End the table schematic
    schematic += '</table>'
    schematic += '<button onclick="addRow_'+name+'()">Add Row</button>'
    schematic += "</fieldset></form>\n"

    return schematic, []



if __name__ == "__main__":
    import json
    import sys

    annotation_scheme = {
        "description": "User Comments",
        "name": "user_comment",
        "labels": ["outline index 1", "outline index 2", "contradiction type"],
        "type": ["text", "text", "text"],
        "select_option": {
            "contradiction type": ["redundant contradiction", "fact contradiction", "might contradiction"]
        },
        "label_width": [10, 10, 10],
        "rows": 5
    }

    schematic, _ = generate_table_layout(annotation_scheme)
    print(schematic)
