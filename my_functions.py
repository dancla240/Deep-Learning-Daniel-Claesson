
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report

def plot_metrics(df_history, style="-o"):
    _, axes = plt.subplots(1, 2, figsize=(12, 4))
    metrics = [["loss", "val_loss"], ["accuracy", "val_accuracy"]]
    for ax, metric in zip(axes, metrics):
        df_history.plot(y=metric, xlabel="Epochs",
                        ylabel=metric[0], title=metric[0],
                        #ylim=(0, 1),
                        ax=ax, style=style)

def plot_metrics_2(history):
	metrics = pd.DataFrame(history)
	metrics[['loss', 'val_loss']].plot()
	metrics[['accuracy', 'val_accuracy']].plot()
     

def plot_confusion_matrix(y_true, y_pred, labels, title="Confusion Matrix", model_name="model_name"):
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt="d", xticklabels=labels, yticklabels=labels)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title(f"Confusion Matrix\n{model_name}")
    plt.show()