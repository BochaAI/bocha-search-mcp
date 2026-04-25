import asyncio  # Add asyncio import
import os
import sys
import time
import json

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()


# Initialize FastMCP server
server = FastMCP(
    "bocha-search-mcp",
    instructions="""
# Bocha Search MCP Server
                 
Bocha is a Chinese search engine for AI, This server provides tools for searching the web using Bocha Search API.
It allows you to get enhanced search details from billions of web documents, including weather, news, wikis, healthcare, train tickets, images, and more.

## Available Tools
                 
### 1. bocha_web_search 
Search with Bocha Web Search and get enhanced search details from billions of web documents, including page titles, urls, summaries, site names, site icons, publication dates, image links, and more.

### 2. bocha_ai_search
Search with Bocha AI Search, recognizes the semantics of search terms and additionally returns structured modal cards with content from vertical domains.

## Output Format

All search results will be formatted as text with clear sections for each
result item, including:

- Bocha Web search: Title, URL, Description, Published date and Site name
- Bocha AI search: Title, URL, Description, Published date, Site name, and structured data card

If the API key is missing or invalid, appropriate error messages will be returned.
"""
)


@server.tool()
async def bocha_web_search(
    query: str, freshness: str = "noLimit", count: int = 10
) -> str:
    """Search with Bocha Web Search and get enhanced search details from billions of web documents,
    including page titles, urls, summaries, site names, site icons, publication dates, image links, and more.

    Args:
        query: Search query (required)
        freshness: The time range for the search results. (Available options YYYY-MM-DD, YYYY-MM-DD..YYYY-MM-DD, noLimit, oneYear, oneMonth, oneWeek, oneDay. Default is noLimit)
        count: Number of results (1-50, default 10)
    """
    # Get API key from environment
    boch_api_key = os.environ.get("BOCHA_API_KEY", "")

    if not boch_api_key:
        return (
            "Error: Bocha API key is not configured. Please set the "
            "BOCHA_API_KEY environment variable."
        )

    # Endpoint
    endpoint = "https://api.bochaai.com/v1/web-search?utm_source=bocha-mcp-local"

    try:
        payload = {
            "query": query,
            "summary": True,
            "freshness": freshness,
            "count": count
        }

        headers = {
            "Authorization": f"Bearer {boch_api_key}",
            "Content-Type": "application/json",
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                endpoint, headers=headers, json=payload, timeout=10.0
            )

            response.raise_for_status()
            resp = response.json()
            if "data" not in resp:
                return "Search error."
            
            data = resp["data"]

            if "webPages" not in data:
                return "No results found."

            results = []
            for result in data["webPages"]["value"]:
                results.append(
                    f"Title: {result['name']}\n"
                    f"URL: {result['url']}\n"
                    f"Description: {result['summary']}\n"
                    f"Published date: {result['datePublished']}\n"
                    f"Site name: {result['siteName']}"
                )

            return "\n\n".join(results)

    except httpx.HTTPStatusError as e:
        return f"Bocha Web Search API HTTP error occurred: {e.response.status_code} - {e.response.text}"
    except httpx.RequestError as e:
        return f"Error communicating with Bocha Web Search API: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@server.tool()
async def bocha_ai_search(
    query: str, freshness: str = "noLimit", count: int = 10
) -> str:
    """Search with Bocha AI Search, recognizes the semantics of search terms
    and additionally returns structured modal cards with content from vertical domains.

    Args:
        query: Search query (required)
        freshness: The time range for the search results. (Available options noLimit, oneYear, oneMonth, oneWeek, oneDay. Default is noLimit)
        count: Number of results (1-50, default 10)
    """
    # Get API key from environment
    boch_api_key = os.environ.get("BOCHA_API_KEY", "")

    if not boch_api_key:
        return (
            "Error: Bocha API key is not configured. Please set the "
            "BOCHA_API_KEY environment variable."
        )

    # Endpoint
    endpoint = "https://api.bochaai.com/v1/ai-search?utm_source=bocha-mcp-local"

    try:
        payload = {
            "query": query,
            "freshness": freshness,
            "count": count,
            "answer": False,
            "stream": False
        }

        headers = {
            "Authorization": f"Bearer {boch_api_key}",
            "Content-Type": "application/json",
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                endpoint, headers=headers, json=payload, timeout=10.0
            )

            response.raise_for_status()
            response = response.json()
            results = []
            if "messages" in response:
                for message in response["messages"]:
                    content = {}
                    try:
                        content = json.loads(message["content"])
                    except:
                        content = {}
                        
                    # 网页
                    if message["content_type"] == "webpage":
                        if "value" in content:
                            for item in content["value"]:
                                results.append(
                                    f"Title: {item['name']}\n"
                                    f"URL: {item['url']}\n"
                                    f"Description: {item['summary']}\n"
                                    f"Published date: {item['datePublished']}\n"
                                    f"Site name: {item['siteName']}"
                                )
                    elif message["content_type"] != "image" and message["content"] != "{}":
                        results.append(message["content"])

            if not results:
                return "No results found."
            
            return "\n\n".join(results)

    except httpx.HTTPStatusError as e:
        return f"Bocha AI Search API HTTP error occurred: {e.response.status_code} - {e.response.text}"
    except httpx.RequestError as e:
        return f"Error communicating with Bocha AI Search API: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"
