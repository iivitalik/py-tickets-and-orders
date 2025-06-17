from django.db import transaction
from django.contrib.auth import get_user_model
from db.models import Order, Ticket


User = get_user_model()


@transaction.atomic
def create_order(tickets: str, username: str, date: int = None) -> None:
    user = User.objects.get(username=username)
    order = Order.objects.create(user=user)
    if date:
        order.created_at = date
        order.save()
    for ticket in tickets:
        Ticket.objects.create(
            order=order,
            row=ticket["row"],
            seat=ticket["seat"],
            movie_session_id=ticket["movie_session"]
        )
    return order


def get_orders(username: str = None) -> None:
    if username:
        return Order.objects.filter(user__username=username)
    return Order.objects.all()
