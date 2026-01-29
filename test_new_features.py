#!/usr/bin/env python3
"""
Test script for new Claude 4.5 features
Based on January 2026 documentation updates
"""

import os
import json
from anthropic import Anthropic

# API key should be set via environment variable
# export ANTHROPIC_API_KEY="your-api-key-here"
if 'ANTHROPIC_API_KEY' not in os.environ:
    print("ERROR: Please set ANTHROPIC_API_KEY environment variable")
    print("  export ANTHROPIC_API_KEY='your-api-key'")
    exit(1)

client = Anthropic()

print("=" * 80)
print("TESTING CLAUDE 4.5 NEW FEATURES")
print("=" * 80)
print()

# Test 1: Claude Sonnet 4.5 - Basic capabilities
print("TEST 1: Claude Sonnet 4.5 - Enhanced Coding & Agents")
print("-" * 80)
try:
    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": "Explain the new Agent SDK in 2-3 sentences. What makes it revolutionary?"
        }]
    )
    print(f"✅ Sonnet 4.5 Response:")
    print(response.content[0].text)
    print(f"Tokens used: Input={response.usage.input_tokens}, Output={response.usage.output_tokens}")
except Exception as e:
    print(f"❌ Error: {e}")
print()

# Test 2: Claude Haiku 3.5 - Speed test (4.5 not available yet)
print("\nTEST 2: Claude Haiku 3.5 - Speed test")
print("-" * 80)
try:
    import time
    start = time.time()
    response = client.messages.create(
        model="claude-3-5-haiku-20241022",
        max_tokens=512,
        messages=[{
            "role": "user",
            "content": "List 5 key benefits of the new Skills system in bullet points."
        }]
    )
    elapsed = time.time() - start
    print(f"✅ Haiku 3.5 Response (took {elapsed:.2f}s):")
    print(response.content[0].text)
    print(f"Tokens used: Input={response.usage.input_tokens}, Output={response.usage.output_tokens}")
    print(f"Note: Haiku 4.5 coming soon - check model availability")
except Exception as e:
    print(f"❌ Error: {e}")
print()

# Test 3: Extended Thinking with Sonnet 4.5
print("\nTEST 3: Extended Thinking (Sonnet 4.5)")
print("-" * 80)
try:
    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=3000,
        thinking={
            "type": "enabled",
            "budget_tokens": 2000  # Minimum 1024 required
        },
        messages=[{
            "role": "user",
            "content": "What are the trade-offs between using Programmatic Tool Calling vs traditional tool use? Think through the pros and cons carefully."
        }]
    )
    print(f"✅ Response with Extended Thinking:")
    for block in response.content:
        if block.type == "thinking":
            thinking_preview = block.thinking[:300] + "..." if len(block.thinking) > 300 else block.thinking
            print(f"\n[THINKING ({len(block.thinking)} chars)] {thinking_preview}")
        elif block.type == "text":
            print(f"\n[RESPONSE] {block.text}")
    print(f"\nTokens used: Input={response.usage.input_tokens}, Output={response.usage.output_tokens}")
except Exception as e:
    print(f"❌ Error: {e}")
print()

# Test 4: Opus 4.5 with Effort Parameter (Beta)
print("\nTEST 4: Claude Opus 4.5 - Effort Parameter (Beta)")
print("-" * 80)
print("Testing different effort levels...")

for effort_level in ["low", "medium", "high"]:
    print(f"\n  Testing effort='{effort_level}':")
    try:
        response = client.beta.messages.create(
            model="claude-opus-4-5-20251101",
            betas=["effort-2025-11-24"],
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": "Explain what the Memory tool does in Claude."
            }],
            output_config={
                "effort": effort_level
            }
        )
        print(f"    ✅ Success! Tokens: {response.usage.output_tokens} output")
        print(f"    Response length: {len(response.content[0].text)} chars")
        if effort_level == "high":
            print(f"    Sample: {response.content[0].text[:150]}...")
    except Exception as e:
        print(f"    ❌ Error: {e}")
print()

# Test 5: Context Awareness (Check model capabilities)
print("\nTEST 5: Model Capabilities Check")
print("-" * 80)
try:
    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=512,
        messages=[{
            "role": "user",
            "content": """I'm building an AI agent system. Based on the new documentation:
            1. Should I use the Agent SDK or build from scratch?
            2. What's the advantage of the Skills system?
            3. How does programmatic tool calling improve efficiency?
            
            Give me actionable advice."""
        }]
    )
    print(f"✅ Context-aware response:")
    print(response.content[0].text)
    print(f"\nTokens used: Input={response.usage.input_tokens}, Output={response.usage.output_tokens}")
except Exception as e:
    print(f"❌ Error: {e}")
print()

# Test 6: Streaming
print("\nTEST 6: Streaming Response")
print("-" * 80)
try:
    print("✅ Streaming: ", end="", flush=True)
    with client.messages.stream(
        model="claude-sonnet-4-5-20250929",
        max_tokens=512,
        messages=[{
            "role": "user",
            "content": "In one paragraph, what's the most exciting feature in the January 2026 Claude update?"
        }]
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
    print("\n")
except Exception as e:
    print(f"❌ Error: {e}")
print()

# Summary
print("\n" + "=" * 80)
print("TEST SUMMARY")
print("=" * 80)
print("""
🔒 SECURITY REMINDER: Rotate your API key NOW!
   Visit: https://console.anthropic.com/settings/keys
""")
print("=" * 80)
