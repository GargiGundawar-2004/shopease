// wishlist.js

async function addToWishlist(productId) {
    try {
        if (!productId) throw new Error("Invalid product");

        console.log("Adding...");

        await fetch('/api/wishlist', {
            method: 'POST',
            body: JSON.stringify({ productId })
        });

        console.log("Added successfully");
    } catch (err) {
        console.error("Wishlist error:", err.message);
    }
}