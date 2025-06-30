from opcua import Client
import time
import os
import re
from audio_generator import (
    speak_text, speak_opcua_value, speak_search_results, 
    speak_error, speak_connection_status, audio_gen
)

def read_trigger_file():
    """Read the trigger file and return its contents"""
    trigger_file = "trigger.txt"
    if os.path.exists(trigger_file):
        try:
            with open(trigger_file, 'r', encoding='utf-8') as f:
                content = f.read()
            return content
        except Exception as e:
            print(f"Error reading trigger file: {e}")
    return None

def extract_tags_and_numbers(transcription):
    """Extract VP, PT, or Tag followed by numbers from transcription"""
    print(f"Analyzing transcription: {transcription}")
    speak_text(f"Analyzing transcription for VP, PT, or Tag patterns")
    
    # Pattern to match VP, PT, or Tag followed by numbers
    pattern = r'\b(VP|PT|Tag)\s*(\d+)\b'
    matches = re.findall(pattern, transcription, re.IGNORECASE)
    
    extracted_tags = []
    for tag_type, number in matches:
        tag_info = {
            'type': tag_type.upper(),
            'number': int(number),
            'search_pattern': f"{tag_type.upper()}{number}"
        }
        extracted_tags.append(tag_info)
        print(f"Found: {tag_type.upper()} {number}")
        speak_text(f"Found {tag_type.upper()} {number}")
    
    return extracted_tags

def search_opcua_nodes(client, tag_pattern):
    """Search for nodes in OPC-UA server that match the tag pattern"""
    try:
        # Get the root node
        root = client.get_root_node()
        
        # Search for nodes containing the tag pattern
        print(f"Searching for nodes containing: {tag_pattern}")
        speak_text(f"Searching for nodes containing {tag_pattern}")
        
        # Method 1: Browse through nodes recursively
        found_nodes = []
        
        def browse_nodes(node, depth=0, max_depth=5):
            if depth > max_depth:
                return
            
            try:
                children = node.get_children()
                for child in children:
                    try:
                        # Get node info
                        node_id = child.nodeid.to_string()
                        browse_name = child.get_browse_name().to_string()
                        display_name = child.get_display_name().to_string()
                        
                        # Check if node matches our pattern
                        if tag_pattern.lower() in browse_name.lower() or tag_pattern.lower() in display_name.lower():
                            found_nodes.append({
                                'node_id': node_id,
                                'browse_name': browse_name,
                                'display_name': display_name,
                                'node': child
                            })
                            print(f"Found matching node: {browse_name} ({node_id})")
                            speak_text(f"Found matching node {browse_name}")
                        
                        # Continue browsing
                        browse_nodes(child, depth + 1, max_depth)
                        
                    except Exception as e:
                        # Skip nodes that can't be accessed
                        continue
                        
            except Exception as e:
                # Skip nodes that can't be browsed
                pass
        
        # Start browsing from root
        browse_nodes(root)
        
        return found_nodes
        
    except Exception as e:
        print(f"Error searching OPC-UA nodes: {e}")
        speak_error(f"Error searching OPC-UA nodes: {e}")
        return []

def read_node_value(client, node_info):
    """Read the value of a specific node"""
    try:
        node = node_info['node']
        value = node.get_value()
        print(f"Node {node_info['browse_name']} value: {value}")
        
        # Speak the value
        speak_opcua_value(node_info['browse_name'], value, "Node")
        
        return value
    except Exception as e:
        print(f"Error reading node value: {e}")
        speak_error(f"Error reading node value: {e}")
        return None

def connect_to_opcua_server(url="opc.tcp://localhost:4840/freeopcua/server/"):
    """Connect to OPC-UA server"""
    client = Client(url)
    try:
        client.connect()
        print(f"Connected to OPC-UA server at {url}")
        speak_connection_status(True, url)
        return client
    except Exception as e:
        print(f"Error connecting to OPC-UA server: {e}")
        speak_connection_status(False, url)
        return None

def process_transcription_and_search(transcription, client):
    """Process transcription and search for tags in OPC-UA server"""
    # Extract tags and numbers
    extracted_tags = extract_tags_and_numbers(transcription)
    
    if not extracted_tags:
        print("No VP, PT, or Tag patterns found in transcription")
        speak_text("No VP, PT, or Tag patterns found in transcription")
        return
    
    print(f"\nFound {len(extracted_tags)} tag(s) to search for:")
    speak_text(f"Found {len(extracted_tags)} tag(s) to search for")
    
    for tag in extracted_tags:
        print(f"- {tag['type']} {tag['number']} (searching for: {tag['search_pattern']})")
    
    all_found_nodes = []
    
    # Search for each tag in OPC-UA server
    for tag in extracted_tags:
        print(f"\n{'='*50}")
        print(f"Searching for {tag['type']} {tag['number']}")
        print(f"{'='*50}")
        
        speak_text(f"Searching for {tag['type']} {tag['number']}")
        
        # Search for nodes matching this tag
        found_nodes = search_opcua_nodes(client, tag['search_pattern'])
        all_found_nodes.extend(found_nodes)
        
        if found_nodes:
            print(f"Found {len(found_nodes)} matching node(s):")
            speak_text(f"Found {len(found_nodes)} matching node(s)")
            
            for i, node_info in enumerate(found_nodes, 1):
                print(f"\n{i}. Node: {node_info['browse_name']}")
                print(f"   ID: {node_info['node_id']}")
                print(f"   Display Name: {node_info['display_name']}")
                
                # Try to read the value
                value = read_node_value(client, node_info)
                if value is not None:
                    print(f"   Value: {value}")
        else:
            print(f"No nodes found matching {tag['search_pattern']}")
            speak_text(f"No nodes found matching {tag['search_pattern']}")
    
    # Speak summary of all results
    speak_search_results(extracted_tags, all_found_nodes)

def main():
    print("OPC-UA Client - Monitoring for trigger file...")
    print("Will search for VP, PT, or Tag patterns in transcribed text")
    speak_text("OPC-UA client started. Monitoring for voice commands.")
    
    # Example OPC-UA server endpoint
    url = "opc.tcp://localhost:4840/freeopcua/server/"
    client = None
    
    try:
        # Monitor for trigger file
        while True:
            content = read_trigger_file()
            if content:
                print("\n" + "="*60)
                print("TRIGGER FILE DETECTED!")
                print("="*60)
                print(content)
                print("="*60)
                
                speak_text("Voice command detected. Processing transcription.")
                
                # Process the transcription
                if "Full transcription:" in content:
                    transcription_part = content.split("Full transcription:")[1].strip()
                    
                    # Connect to OPC-UA server
                    client = connect_to_opcua_server(url)
                    if client:
                        # Process transcription and search for tags
                        process_transcription_and_search(transcription_part, client)
                        client.disconnect()
                        print("Disconnected from OPC-UA server")
                        speak_text("OPC-UA operations completed")
                    else:
                        print("Failed to connect to OPC-UA server")
                        speak_text("Failed to connect to OPC-UA server")
                
                # Remove the trigger file to avoid reprocessing
                try:
                    os.remove("trigger.txt")
                    print("Trigger file removed")
                except Exception as e:
                    print(f"Error removing trigger file: {e}")
            
            time.sleep(1)  # Check every second
            
    except KeyboardInterrupt:
        print("\nStopping OPC-UA client...")
        speak_text("Stopping OPC-UA client")
    except Exception as e:
        print(f"Error in main loop: {e}")
        speak_error(f"Error in main loop: {e}")
    finally:
        if client:
            client.disconnect()
            print("Disconnected from OPC-UA server.")
        audio_gen.stop()

if __name__ == "__main__":
    main() 