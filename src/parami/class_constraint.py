from parami.file_operations import *
from parami.bootstrap import *
from pathlib import Path
import hashlib
import pickle
import os


class Constraint:
    """Defines the 'Constraint' class.

    Constraints are derived from entries, each instance represents a real constraint which is places on the value of the entry.
    Upon creation a constraint generates an identifier which combines its own hash with the hash of the related entry.
    Instances are stored as pickles in the 'constraints' directory. The instance can test itself.

    Attributes:
        id        (str): The identifier, createn by hashing 'operator' and 'condition'.
        key       (str): Inherited from an entry.
        value     (multiple): Inherited from an entry.
        operator  (str): The operator that the value will be compared by.
        condition (multiple): The condition that the value will be compared against.
        result    (bool): The result of the instance testing itself.

    """

    def __init__(
        self,
        id: str,
        key: str,
        value: float | int | str,
        operator: str,
        condition: float | int | str,
        result: bool = None,
    ):
        """
        Initiate the 'Constraint' instance.
        """
        self.Id = id + "-" + self.identifier(operator, condition)
        self.Key = key
        self.Value = value
        self.Type = type(value).__name__
        self.Operator = operator
        self.Condition = condition
        self.Result = result
        self.test()
        self.save()

    def save(self) -> None:
        """
        Save the 'Constraint' instance as a pickle.
        """

        with open(self.path(), "wb") as file:
            pickle.dump(self, file)

    def load(self) -> None:
        """
        Load the 'Constraint' instance from a pickle.
        """

        with open(self.path(), "rb") as file:
            return pickle.load(file)

    def delete(self) -> None:
        """
        Delete the 'Constraint' instance by removing the pickle.
        """

        os.remove(self.path())

    def path(self) -> Path:
        """
        Return the path of the instance pickle.
        """

        return Path(f"/tmp") / "parami" / "objects" / "constraints" / f"{self.Id}.pkl"

    def test(self) -> None:
        """
        Tests the constraint and returns the result.
        """

        if type(self.Value) is str and type(self.Condition) is str:
            self.Result = test_constraint_string(
                value=self.Value, operator=self.Operator, condition=self.Condition
            )

        elif type(self.Value) is str and type(self.Condition) is int or float:
            self.Result = test_constraint_string(
                value=str(self.Value),
                operator=self.Operator,
                condition=str(self.Condition),
            )

        elif type(self.Value) is int or float and type(self.Condition) is str:
            self.Result = test_constraint_string(
                value=str(self.Value),
                operator=self.Operator,
                condition=str(self.Condition),
            )

        elif type(self.Value) is int or float and type(self.Condition) is int or float:
            self.Result = test_constraint_number(
                value=self.Value, operator=self.Operator, condition=self.Condition
            )

        return self.Result

    def value(self) -> None:
        """
        Set the 'value' property.
        """

        return self.Value

    @staticmethod
    def identifier(x, y) -> hex:
        """
        Create an identifier and return it.
        """

        return hashlib.md5(f"{x}:{y}".encode("utf-8")).hexdigest()


def equals(x, y) -> bool:
    """
    Compare two factors to find out if they are equal, returns a boolean.

    Args:
        x (multiple): The first factor.
        y (multiple): The second factor.

    Returns:
        Bool True or False.
    """

    return y == x


def notequals(x, y) -> bool:
    """
    Compare two factors to find out if they are not equal, returns a boolean.

    Args:
        x (multiple): The first factor.
        y (multiple): The second factor.

    Returns:
        Bool True or False.
    """

    return y != x


def greaterequals(x, y) -> bool:
    """
    Compare two factors to find out if one is greater than or equal to the other, returns a boolean.

    Args:
        x (multiple): The first factor.
        y (multiple): The second factor.

    Returns:
        Bool True or False.
    """

    return x >= y


def lesserequals(x, y) -> bool:
    """
    Compare two factors to find out if one is lesser than or equal to the other, returns a boolean.

    Args:
        x (multiple): The first factor.
        y (multiple): The second factor.

    Returns:
        Bool True or False.
    """

    return x <= y


def max(x, y) -> bool:
    """
    Compare two factors to find out if one exceeds the other, returns a boolean.

    Args:
        x (multiple): The first factor.
        y (multiple): The second factor.

    Returns:
        Bool True or False.
    """

    return y > x


def min(x, y) -> bool:
    """
    Compare two factors to find out if one is exceeded by the other, returns a boolean.

    Args:
        x (multiple): The first factor.
        y (multiple): The second factor.

    Returns:
        Bool True or False.
    """

    return y < x


def test_constraint_string(value: str, operator: str, condition: str) -> bool:
    """
    Take a string as value, operator and condition from a constraint and test it.
    In all cases except 'is' and 'not' a string will be evaluated by length.

    Args:
        value     (str): The value passed from the constraint.
        operator  (str): The operator passed from the constraint.
        condition (str): The condition passed from the constraint.

    Returns:
        Bool True or False.
    """

    len_value = len(value)
    len_condition = len(condition)

    match operator:
        case "equals" | "eq" | "==":
            return equals(len_value, len_condition)

        case "notequals" | "ne" | "!=":
            return notequals(len_value, len_condition)

        case "greaterequals" | "ge" | ">=":
            return greaterequals(len_value, len_condition)

        case "lesserequals" | "le" | "<=":
            return lesserequals(len_value, len_condition)

        case "max" | "lt" | "<":
            return max(len_value, len_condition)

        case "min" | "gt" | ">":
            return min(len_value, len_condition)

        case "is":
            return equals(value, condition)

        case "isnt" | "not":
            return notequals(value, condition)

        case _:
            return "Invalid"


def test_constraint_number(
    value: int | float, operator: str, condition: int | float
) -> bool:
    """
    Take an int or float as value, operator and condition from a constraint and test it.

    Args:
        value     (multiple): The value passed from the constraint.
        operator  (multiple): The operator passed from the constraint.
        condition (multiple): The condition passed from the constraint.

    Returns:
        Bool True or False.
    """

    match operator:
        case "equals" | "eq" | "is" | "==":
            return equals(value, condition)

        case "notequals" | "ne" | "isnt" "!=":
            return notequals(value, condition)

        case "greaterequals" | "ge" | ">=":
            return greaterequals(value, condition)

        case "lesserequals" | "le" | "<=":
            return lesserequals(value, condition)

        case "max" | "lt" | "<":
            return max(value, condition)

        case "min" | "gt" | ">":
            return min(value, condition)

        case _:
            return "Invalid"
