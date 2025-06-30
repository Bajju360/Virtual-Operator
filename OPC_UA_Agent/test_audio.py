#!/usr/bin/env python3
"""
Test script for the Audio Generator
Run this to test the text-to-speech functionality
"""

from audio_generator import (
    speak_text, speak_opcua_value, speak_search_results, 
    speak_error, speak_connection_status, audio_gen
)
import time

def test_basic_speech():
    """Test basic text-to-speech functionality"""
    print("Testing basic speech...")
    speak_text("Hello, this is a test of the audio generator")
    time.sleep(2)

def test_opcua_values():
    """Test OPC-UA value announcements"""
    print("Testing OPC-UA value announcements...")
    
    # Test different value types
    speak_opcua_value("VP123", 25.5, "VP")
    time.sleep(2)
    
    speak_opcua_value("PT456", 100, "PT")
    time.sleep(2)
    
    speak_opcua_value("Tag789", "Running", "Tag")
    time.sleep(2)

def test_search_results():
    """Test search result announcements"""
    print("Testing search result announcements...")
    
    # Simulate found tags and nodes
    found_tags = [
        {'type': 'VP', 'number': 123},
        {'type': 'PT', 'number': 456}
    ]
    
    found_nodes = [
        {'browse_name': 'VP123_Temperature'},
        {'browse_name': 'PT456_Pressure'}
    ]
    
    speak_search_results(found_tags, found_nodes)
    time.sleep(3)

def test_error_messages():
    """Test error message announcements"""
    print("Testing error message announcements...")
    speak_error("Connection failed to OPC-UA server")
    time.sleep(2)

def test_connection_status():
    """Test connection status announcements"""
    print("Testing connection status announcements...")
    
    # Test successful connection
    speak_connection_status(True, "opc.tcp://localhost:4840/freeopcua/server/")
    time.sleep(2)
    
    # Test failed connection
    speak_connection_status(False, "opc.tcp://localhost:4840/freeopcua/server/")
    time.sleep(2)

def test_voice_settings():
    """Test different voice settings"""
    print("Testing voice settings...")
    
    # Test slower speech
    print("Testing slower speech rate...")
    audio_gen.set_voice_rate(100)
    speak_text("This is slower speech for better understanding")
    time.sleep(3)
    
    # Test faster speech
    print("Testing faster speech rate...")
    audio_gen.set_voice_rate(200)
    speak_text("This is faster speech for quick updates")
    time.sleep(3)
    
    # Reset to default
    audio_gen.set_voice_rate(150)

def test_queue_functionality():
    """Test speech queue functionality"""
    print("Testing speech queue functionality...")
    
    # Add multiple messages to queue
    speak_text("First message in queue")
    speak_text("Second message in queue")
    speak_text("Third message in queue")
    
    print("Added 3 messages to queue. They should play in sequence...")
    time.sleep(8)  # Wait for all messages to complete

def main():
    """Main test function"""
    print("=" * 60)
    print("AUDIO GENERATOR TEST")
    print("=" * 60)
    print("This will test all audio generator functionality.")
    print("Make sure your speakers are on and volume is up!")
    print("=" * 60)
    
    try:
        # Test basic functionality
        test_basic_speech()
        
        # Test OPC-UA specific functions
        test_opcua_values()
        
        # Test search results
        test_search_results()
        
        # Test error messages
        test_error_messages()
        
        # Test connection status
        test_connection_status()
        
        # Test voice settings
        test_voice_settings()
        
        # Test queue functionality
        test_queue_functionality()
        
        print("\n" + "=" * 60)
        print("ALL TESTS COMPLETED!")
        print("=" * 60)
        
        # Final test message
        speak_text("Audio generator test completed successfully!")
        
    except KeyboardInterrupt:
        print("\nTest interrupted by user")
        speak_text("Test interrupted")
    except Exception as e:
        print(f"Error during test: {e}")
        speak_error(f"Test error: {e}")
    finally:
        # Cleanup
        audio_gen.stop()
        print("Audio generator stopped")

if __name__ == "__main__":
    main() 