from rules import predicate

from ej_conversations.models import Conversation, Comment
from .models import GivenPower, CommentPromotion, GivenBridgePower, GivenMinorityPower


@predicate
def has_opinion_bridge_power(user, conversation):
    """
    Return true if user is a "opinion bridge" in conversation.
    """
    return GivenBridgePower.objects.filter(user=user, conversation=conversation).exists()


@predicate
def can_be_opinion_bridge(user, conversation):
    """
    Opinion bridges sits between two clusters and may help to promote dialogue
    between both clusters.
    """


@predicate
def has_activist_power(user, conversation):
    return GivenMinorityPower.objects.filter(user=user, conversation=conversation).exists()


@predicate
def can_be_activist(user, conversation):
    """
    Activist is someone that is in a cluster and agrees with most opinions, but
    has some divergent opinion
    """
    pass


#
# Powers
#


def promoted_comments(user, conversation):
    """
    Return all comments promoted in a conversation for a user
    """
    if not user.is_authenticated:
        return Comment.objects.none()
    else:
        promotions = Promotion.timeframed.filter(comment__conversation=conversation, users=user)
        return Comment.objects.filter(promotions__in=promotions)