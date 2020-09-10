from gitgud.skills.level_builder import BasicLevel
from gitgud.skills.util import Skill

skill = Skill(
    'New Basics',
    'newbasics',
    [
        BasicLevel('Two Commits', 'twocommits', __name__)
    ]
)
