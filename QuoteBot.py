# bot.py
import json
from twitchio.ext import commands

class QuoteBot(commands.Bot):

    def __init__(self):
        super().__init__(token='YOUR_TWITCH_TOKEN', prefix='!', initial_channels=['YOUR_CHANNEL'])
        self.quotes = self.load_quotes()

    def load_quotes(self):
        try:
            with open('quotes.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_quotes(self):
        with open('quotes.json', 'w') as f:
            json.dump(self.quotes, f)

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

    async def event_message(self, message):
        # Ignore messages from the bot itself
        if message.author.name.lower() == self.nick.lower():
            return

        # Process commands
        await self.handle_commands(message)

    @commands.command(name='addquote')
    async def add_quote(self, ctx, *, quote: str):
        user_name = ctx.author.name
        quote_number = len(self.quotes) + 1  # Increment quote number based on current list length
        formatted_quote = f"{quote_number}: {user_name}: \"{quote}\""
        self.quotes.append(formatted_quote)
        self.save_quotes()
        await ctx.send(f'Quote added: "{formatted_quote}"')

    @commands.command(name='quotes')
    async def list_quotes(self, ctx):
        if not self.quotes:
            await ctx.send("No quotes available.")
            return
        quotes_list = "\n".join(self.quotes)
        await ctx.send(f"Quotes:\n{quotes_list}")

    @commands.command(name='searchquote')
    async def search_quote(self, ctx, *, query: str):
        results = []
        
        # Check if the query is a number (for quote number)
        if query.isdigit():
            index = int(query) - 1  # Convert to zero-based index
            if 0 <= index < len(self.quotes):
                results.append(self.quotes[index])
            else:
                await ctx.send(f"No quote found with number {query}.")
                return
        else:
            # Search for the keyword in quotes
            results = [quote for quote in self.quotes if query.lower() in quote.lower()]

        # Count total quotes
        total_quotes = len(self.quotes)

        if results:
            results_list = "\n".join(results)
            await ctx.send(f"Search results:\n{results_list}\nTotal quotes available: {total_quotes}")
        else:
            await ctx.send(f"No quotes found matching '{query}'. Total quotes available: {total_quotes}.")

    @commands.command(name='quote_count')
    async def quote_count(self, ctx):
        total_quotes = len(self.quotes)
        await ctx.send(f"Total quotes available: {total_quotes}")

if __name__ == "__main__":
    bot = QuoteBot()
    bot.run()
