class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Superhero:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name

class DecisionTree:
    def __init__(self, decision_tree):
        self.decision_tree = decision_tree

    def assign_superhero(self):
        current_node = self.decision_tree

        while True:
            if isinstance(current_node.data, Superhero):
                return current_node.data
            else:
                answer = input(f"{current_node.data} (Yes/No): ")
                if answer.lower() == "yes" or answer.lower() == "y":
                    current_node = current_node.left
                else:
                    current_node = current_node.right

def main():
    # Create superheroes
    iron_man = Superhero("Iron Man", "Leader for planning defense missions, genius and advanced technology expert")
    hulk = Superhero("The Incredible Hulk", "Excellent choice for destruction missions")
    khan = Superhero("Khan", "Ideal for intergalactic team missions")
    thor = Superhero("Thor", "Power to destroy entire armies")
    cap_america = Superhero("Captain America", "Supersoldier with unbreakable ethics, ideal for commanding defense and recovery missions")
    cap_marvel = Superhero("Captain Marvel", "Very powerful and able to travel across galaxies")
    ant_man = Superhero("Ant-Man", "Excellent in recovery missions where undetection is necessary")
    nick_fury = Superhero("Nick Fury", "The most logical choice for deciding the next action and quickly moving from one place to another")
    winter_soldier = Superhero("The Winter Soldier", "Ideal for recovery missions requiring infiltration among locals")

    # Create balanced decision tree
    decision_tree = TreeNode("Is the mission a recovery mission?")

    decision_tree.left = TreeNode("Is infiltration among locals necessary?")
    decision_tree.right = TreeNode("Is the mission intergalactic?")

    decision_tree.left.left = TreeNode(winter_soldier)
    decision_tree.left.right = TreeNode(ant_man)

    decision_tree.right.left = TreeNode("Is the mission a team mission?")
    decision_tree.right.right = TreeNode("Is the mission a defense mission?")

    decision_tree.right.left.left = TreeNode(khan)
    decision_tree.right.left.right = TreeNode(cap_marvel)

    decision_tree.right.right.left = TreeNode("Does the mission require advanced technology?")
    

    decision_tree.right.right.left.left = TreeNode(iron_man)
    decision_tree.right.right.left.right = TreeNode(nick_fury)

    decision_tree.right.right.right.left = TreeNode("Are there entire armies?")
    

    decision_tree.right.right.right.left.left = TreeNode(thor)
    decision_tree.right.right.right.left.right = TreeNode(cap_america)

    # Example usage
    tree = DecisionTree(decision_tree)
    selected_hero = tree.assign_superhero()
    print(f"\nSelected hero: {selected_hero}\nDescription: {selected_hero.description}")

if __name__ == "__main__":
    main()
