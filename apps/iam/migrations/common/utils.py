from django.db import migrations

def generate_default_boolean_field_migration(table_name: str, column_name: str, default_value: bool):
    def forwards(_apps, schema_editor):
        schema_editor.execute(f'ALTER TABLE IF EXISTS {table_name} ALTER COLUMN {column_name} SET DEFAULT {default_value};')
    def backwards(_apps, schema_editor):
        schema_editor.execute(f'ALTER TABLE IF EXISTS {table_name} ALTER COLUMN {column_name} DROP DEFAULT;')
    return (forwards, backwards)
        

def generate_default_datetime_field_migration(table_name: str, column_name: str):
    def forwards(_apps, schema_editor):
        schema_editor.execute(f'ALTER TABLE IF EXISTS {table_name} ALTER COLUMN {column_name} SET DEFAULT NOW();')
    def backwards(_apps, schema_editor):
        schema_editor.execute(f'ALTER TABLE IF EXISTS {table_name} ALTER COLUMN {column_name} DROP DEFAULT;')
    return (forwards, backwards)
    
def generate_default_uuid_field_migration(table_name: str, column_name: str):
    def forwards(_apps, schema_editor):
        schema_editor.execute(f'ALTER TABLE IF EXISTS {table_name} ALTER COLUMN {column_name} SET DEFAULT gen_random_uuid();')
    def backwards(_apps, schema_editor):
        schema_editor.execute(f'ALTER TABLE IF EXISTS {table_name} ALTER COLUMN {column_name} DROP DEFAULT;')
    return (forwards, backwards)

def add_is_active_default_migration(table_name: str):
    (forwards, backwards) = generate_default_boolean_field_migration(table_name, 'is_active', False)
    return migrations.RunPython(
        forwards,
        backwards
    )

def add_datetime_base_fields_default_migration(table_name: str):
    (created_at_forwards, created_at_backwards) = generate_default_datetime_field_migration(table_name, 'created_at')
    
    (updated_at_forwards, updated_at_backwards) = generate_default_datetime_field_migration(table_name, 'updated_at')
    return [migrations.RunPython(
        created_at_forwards, created_at_backwards
    ), migrations.RunPython(
        updated_at_forwards, updated_at_backwards
    )]

def add_default_id_field(table_name: str):
    (forwards, backwards) = generate_default_uuid_field_migration(table_name, 'id')
    return migrations.RunPython(
        forwards, backwards
    )

def add_base_field_default(table_name: str):
    return [
        add_is_active_default_migration(table_name),
        *add_datetime_base_fields_default_migration(table_name),
        add_default_id_field(table_name)
    ]
