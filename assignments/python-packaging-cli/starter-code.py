"""Starter code for the Python Project Packaging and CLI Tools assignment."""

import argparse
import logging


logger = logging.getLogger(__name__)


def add_task(tasks, description):
    """Add a task and return its new numeric ID."""
    # TODO: Store the task and return its ID.
    raise NotImplementedError


def list_tasks(tasks):
    """Return a display-ready list of tasks."""
    # TODO: Return each task with its completion state.
    raise NotImplementedError


def complete_task(tasks, task_id):
    """Mark a task as complete and return whether it was found."""
    # TODO: Find the task by ID and mark it complete.
    raise NotImplementedError


def build_parser():
    parser = argparse.ArgumentParser(description="Manage a small task list")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a task")
    add_parser.add_argument("description")

    subparsers.add_parser("list", help="List tasks")

    complete_parser = subparsers.add_parser("complete", help="Complete a task")
    complete_parser.add_argument("task_id", type=int)

    return parser


def main():
    # TODO: Parse arguments, call the appropriate function, and configure logging.
    parser = build_parser()
    parser.parse_args()
    logger.info("Task CLI started")


if __name__ == "__main__":
    main()
