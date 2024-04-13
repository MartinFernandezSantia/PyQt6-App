from PyQt6.QtWidgets import QVBoxLayout, QLabel

def labeled_widget(label_text: str, widget):
    """ Crea un layout vertical (QVBoxLayout) con un espacio entre widgets de 0
    y añade al mismo un label (QLabel) y un widget. A continuación se agrega este
    layout dentro del 'parent_layout'

    Args:
        label_text (str): "Ejemplo de texto de Label"
        widget (PyQt6 Widget): PyQt6.QtWidgets.QComboBox()
        parent_layout (PyQt6 Layout): PyQt6.QtWidgets.QVBoxLayout()

    Returns QVBoxLayout()
    """
    new_layout = QVBoxLayout()
    new_layout.setSpacing(0)

    label = QLabel(label_text)

    new_layout.addWidget(label)
    new_layout.addWidget(widget)

    return new_layout
