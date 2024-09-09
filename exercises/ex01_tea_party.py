"""Creating a program to help plan a cozy tea party"""

__author__: str = "730580155"


def main_planner(guests: int) -> None:
    """main planning the tea party function"""
    print("A Cozy Tea Party for", guests, "People")
    print("Tea Bags:", tea_bags(people=guests))
    print("Treats:", treats(people=guests))
    print(
        "Cost: $"
        + str(
            (cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests)))
        ),
    )


def tea_bags(people: int) -> int:
    """how many tea bags are needed at the party"""
    return people * 2


def treats(people: int) -> int:
    """how many treats are needed at the party"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """how much the tea and treats will cost"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
