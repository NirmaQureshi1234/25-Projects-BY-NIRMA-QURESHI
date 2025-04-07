import random

class MarkovChain:
    def __init__(self):
        self.model = {}

    def train(self, text, order=2):
        """Train the Markov model on the given text."""
        words = text.split()
        for i in range(len(words) - order):
            # Create a tuple of the current sequence of words
            state = tuple(words[i:i + order])
            next_word = words[i + order]

            # Add the next word to the model
            if state not in self.model:
                self.model[state] = []
            self.model[state].append(next_word)

    def generate(self, seed, length=50):
        """Generate text using the trained Markov model."""
        # Convert the seed into a tuple
        current_state = tuple(seed.split())

        # Ensure the seed is in the model
        if current_state not in self.model:
            raise ValueError("Seed not found in the model.")

        output = list(current_state)
        for _ in range(length):
            # Check if the current state exists in the model
            if current_state not in self.model:
                break  # Stop if the state is not found

            # Get the next word from the model
            next_word = random.choice(self.model[current_state])
            output.append(next_word)

            # Update the current state
            current_state = tuple(output[-len(current_state):])

        return " ".join(output)


# Example usage
if __name__ == "__main__":
    # Input text (can be replaced with a file read)
    text = """
    This is a simple example of a Markov chain. A Markov chain is a stochastic model 
    that describes a sequence of possible events. Each event depends only on the state 
    attained in the previous event. This is what makes it a Markov process.
    """

    # Create and train the Markov chain
    markov = MarkovChain()
    markov.train(text, order=2)  # Use order=2 for bigrams

    # Generate text
    seed = "This is"
    try:
        generated_text = markov.generate(seed, length=20)
        print("Generated Text:")
        print(generated_text)
    except ValueError as e:
        print(e)