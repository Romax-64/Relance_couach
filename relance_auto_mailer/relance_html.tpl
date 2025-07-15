<!DOCTYPE html>
<html lang="{{ 'fr' if is_fr else 'en' }}">
<head>
    <meta charset="UTF-8">
    <title>{% if is_fr %}Suivi commandes en cours{% else %}Order Follow-up{% endif %}</title>
</head>
<body>
    <p>{% if is_fr %}Bonjour,{% else %}Hello,{% endif %}</p>
    <p>{% if is_fr %}Je viens vers vous concernant les commandes que nous avons en cours chez vous :{% else %}I am contacting you regarding the orders we currently have with your company:{% endif %}</p>
    <ul>
    {% for cmd in commandes %}
        <li><strong>{% if is_fr %}Commande n°{% else %}Order no.{% endif %} {{ cmd.num_achat }}</strong>, {% if is_fr %}article{% else %}item{% endif %} {{ cmd.fourniture }}, {% if is_fr %}initialement prévue pour le{% else %}initially scheduled for{% endif %} {{ cmd.date_promise }}</li>
    {% endfor %}
    </ul>
    <p>
    {% if is_fr %}
    Nous n'avons à ce jour pas reçu de mise à jour concernant leur livraison.<br>
    Pourriez-vous nous communiquer les nouvelles dates de livraison ou tout document pouvant justifier du transport ou de la livraison de ces produits ?
    {% else %}
    To date, we have not received any update regarding their delivery.<br>
    Could you please provide us with the new delivery dates, or any document that could justify the transport or shipment of these products?
    {% endif %}
    </p>
    <p>{% if is_fr %}Merci d'avance pour votre retour rapide,{% else %}Thank you in advance for your prompt response.{% endif %}<br>
    {% if is_fr %}Cordialement.{% else %}Best regards.{% endif %}</p>
    <p><strong>{{ signature }}</strong></p>
</body>
</html>