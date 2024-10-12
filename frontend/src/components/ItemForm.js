import React, { useState } from 'react';
import axios from '../api/api';

function ItemForm() {
    const [name, setName] = useState('');
    const [quantity, setQuantity] = useState(1);

    const handleSubmit = async (e) => {
        e.preventDefault();
        await axios.post('/items', { name, quantity });
        setName('');
        setQuantity(1);
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Add Item</h2>
            <input
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="Item Name"
                required
            />
            <input
                type="number"
                value={quantity}
                onChange={(e) => setQuantity(e.target.value)}
                min="1"
                required
            />
            <button type="submit">Add Item</button>
        </form>
    );
}

export default ItemForm;

