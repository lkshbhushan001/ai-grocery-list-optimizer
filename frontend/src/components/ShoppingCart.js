import React from 'react';

function ShoppingCart({ items }) {
    return (
        <div>
            <h2>Your Shopping Cart</h2>
            <ul>
                {items.map(item => (
                    <li key={item.id}>{item.name} (x{item.quantity})</li>
                ))}
            </ul>
        </div>
    );
}

export default ShoppingCart;
