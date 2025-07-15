{% if is_fr %}
Bonjour,

Je viens vers vous concernant les commandes que nous avons en cours chez vous :
{% else %}
Hello,

I am contacting you regarding the orders we currently have with your company:
{% endif %}

{% for cmd in commandes %}
{% if is_fr %}- Commande n° {{ cmd.num_achat }}, article {{ cmd.fourniture }}, initialement prévue pour le {{ cmd.date_promise }}
{% else %}- Order no. {{ cmd.num_achat }}, item {{ cmd.fourniture }}, initially scheduled for {{ cmd.date_promise }}
{% endif %}
{% endfor %}

{% if is_fr %}
Nous n'avons à ce jour pas reçu de mise à jour concernant leur livraison.
Pourriez-vous nous communiquer les nouvelles dates de livraison ou tout document pouvant justifier du transport ou de la livraison de ces produits ?

Merci d'avance pour votre retour rapide,
Cordialement.
{% else %}
To date, we have not received any update regarding their delivery.
Could you please provide us with the new delivery dates, or any document that could justify the transport or shipment of these products?

Thank you in advance for your prompt response.
Best regards.
{% endif %}

{{ signature }}