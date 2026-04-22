// wishlist.js

async function addToWishlist(productId) {
    if (!productId) {
        throw new Error("Invalid product");
    }

    await fetch('/api/wishlist', {
        method: 'POST',
        body: JSON.stringify({ productId })
    });
}