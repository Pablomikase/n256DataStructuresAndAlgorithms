class Group:
    """
    A class to represent a group which can contain sub-groups and users.

    Attributes:
    -----------
    name : str
        The name of the group.
    groups : list[Group]
        A list of sub-groups within this group.
    users : list[str]
        A list of users in this group.
    """

    def __init__(self, _name: str) -> None:
        """
        Constructs all the necessary attributes for the Group object.

        Parameters:
        -----------
        _name : str
            The name of the group.
        """
        self.name: str = _name
        self.groups: list[Group] = []
        self.users: list[str] = []

    def add_group(self, group: 'Group') -> None:
        """
        Add a sub-group to this group.

        Parameters:
        -----------
        group : Group
            The sub-group to be added.
        """
        self.groups.append(group)

    def add_user(self, user: str) -> None:
        """
        Add a user to this group.

        Parameters:
        -----------
        user : str
            The user to be added.
        """
        self.users.append(user)

    def get_groups(self) -> list['Group']:
        """
        Get the list of sub-groups in this group.

        Returns:
        --------
        list[Group]
            A list of sub-groups.
        """
        return self.groups

    def get_users(self) -> list[str]:
        """
        Get the list of users in this group.

        Returns:
        --------
        list[str]
            A list of users.
        """
        return self.users

    def get_name(self) -> str:
        """
        Get the name of this group.

        Returns:
        --------
        str
            The name of the group.
        """
        return self.name


def is_user_in_group(user: str, group: Group) -> bool:
    """
    Check if a user is in the given group or any of its sub-groups.

    Parameters:
    -----------
    user : str
        The user to be checked.
    group : Group
        The group in which to search for the user.

    Returns:
    --------
    bool
        True if the user is found in the group or any sub-group, False otherwise.
    """
    if user is None:
        return False

    # Use a stack to implement an iterative depth-first search
    stack = [group]

    while stack:
        current_group = stack.pop()
        # Check if the user is directly in this group
        if user in current_group.get_users():
            return True

        # Add all subgroups to the stack for further exploration
        stack.extend(current_group.get_groups())

    return False

if __name__ == "__main__":
    # Testing the implementation

    # Creating groups and users
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    # Test Case 1: User is in a nested subgroup
    print("Test Case 1")
    print(is_user_in_group("sub_child_user", parent))  # Expected output: True

    # Test Case 2: User is not in the group
    print("Test Case 2")
    print(is_user_in_group("random_user", parent))  # Expected output: False

    # Test Case 3: User is directly in the parent group
    parent_user = "parent_user"
    parent.add_user(parent_user)
    print("Test Case 3")
    print(is_user_in_group("parent_user", parent))  # Expected output: True

    # Test Case 4: User is directly in a child group
    child_user = "child_user"
    child.add_user(child_user)
    print("Test Case 4")
    print(is_user_in_group("child_user", parent))  # Expected output: True

    # Test Case 5: User is None
    print("Test Case 5")
    print(is_user_in_group(None, parent))  # Expected output: False

    # Test Case 7: Both user and group are None
    print("Test Case 7")
    print(is_user_in_group(None, None))  # Expected output: False

    # Test Case 8: User is an empty string
    print("Test Case 8")
    print(is_user_in_group("", parent))  # Expected output: False

    # Test Case 9: Empty group (no users, no sub-groups)
    empty_group = Group("empty_group")
    print("Test Case 9")
    print(is_user_in_group("any_user", empty_group))  # Expected output: False

    # Test Case 10: Large nested structure
    deep_parent = Group("deep_parent")
    level_1 = Group("level_1")
    level_2 = Group("level_2")
    level_3 = Group("level_3")
    level_4 = Group("level_4")

    level_4.add_user("deep_user")
    level_3.add_group(level_4)
    level_2.add_group(level_3)
    level_1.add_group(level_2)
    deep_parent.add_group(level_1)

    print("Test Case 10")
    print(is_user_in_group("deep_user", deep_parent))  # Expected output: True
