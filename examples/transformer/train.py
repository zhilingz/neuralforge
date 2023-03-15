"""Training example: WikiText with Transformer."""
import neuralforge as nf
from neuralforge.nn import Module
from neuralforge.optim import Adam
from neuralforge.data import DataLoader, Dataset

class SimpleDataset(Dataset):
    def __len__(self):
        return 1000

    def __getitem__(self, idx):
        return nf.Tensor([0.0] * 784), idx % 10

def main():
    dataset = SimpleDataset()
    loader = DataLoader(dataset, batch_size=32, shuffle=True)
    model = Module()  # Placeholder for Transformer
    optimizer = Adam(model.parameters(), lr=0.001)

    for epoch in range(20):
        for batch in loader:
            optimizer.zero_grad()
            # forward + backward + step
            optimizer.step()
        print(f"Epoch {epoch+1}/20 complete")

if __name__ == "__main__":
    main()
